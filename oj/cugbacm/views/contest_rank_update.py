#!/usr/bin/env python
from datetime import *
import time
import datetime
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from cugbacm.proto import rank_pb2
from celery.task import task
import ssdb_api
#import ssdb_api
class Rank():
  class Problem():
    class Submit():
      def __init__(self, runID = "", status="", date_time=""):
        self.status = status
        self.date_time = date_time
        self.runID = runID

    def __init__(self, problemID):
      self.problemID = problemID
      self.submit_list = []
      self.acindex = 0
      self.totalindex = 0
      self.time = 0
      self.FB = 0

    def add_submit(self, submit):
      self.submit_list.append(submit)

  def __init__(self, userID, contestID):
    self.userID = userID
    self.contestID = contestID
    self.problem_list = {}
    self.ac = 0
    self.penalty = 0
    self.total = 0

  def load_data_to_proto(self, rank):
    rank.userID = self.userID
    rank.contestID = self.contestID
    rank.ac = self.ac
    rank.penalty = self.penalty
    rank.total = self.total

    for problemID in self.problem_list:
      problem = self.problem_list[problemID]
      p = rank.problem.add()
      p.problemID = problem.problemID
      p.acindex = problem.acindex
      p.totalindex = problem.totalindex
      p.time = problem.time
      p.FB = problem.FB
      for submit in problem.submit_list:
        s = p.submit.add()
        s.status = submit.status
        s.date_time = submit.date_time
        s.runID = submit.runID
    return rank

def sort_rank(rank_list, contest_id, FB):
  contest = Contest.objects.get(contestID = contest_id)
  st_time = str(contest.startTime) + " " + str(contest.startTimestamp)
  ST_time =  datetime.datetime.strptime(st_time, "%Y-%m-%d %H:%M:%S")
  for userID in rank_list:
    rank = rank_list[userID]
    for problem in rank.problem_list:
      for submit in rank.problem_list[problem].submit_list:
        rank.total = rank.total + 1
        if submit.status == "Accepted":
          if rank.problem_list[problem].acindex == 0:
            rank.ac = rank.ac + 1
            rank.problem_list[problem].totalindex = rank.problem_list[problem].totalindex + 1
            rank.problem_list[problem].acindex = 1
            P_time = datetime.datetime.strptime(submit.date_time, "%Y-%m-%d %H:%M:%S")
            d = (P_time - ST_time).seconds + (P_time - ST_time).days*24*60*60
            rank.penalty = rank.penalty + d
            rank.problem_list[problem].time = rank.problem_list[problem].time + d
        elif (rank.problem_list[problem].acindex != 1):
          rank.problem_list[problem].totalindex = rank.problem_list[problem].totalindex + 1
          rank.problem_list[problem].time = rank.problem_list[problem].time + 1200
  #rank_list = sorted(rank_list, cmp = lambda x,y:cmp(x[1].ac, y[1].ac) or cmp(x[1].penalty, y[1].penalty))
  #rank_list.sorted(lambda x, y: cmp(x.ac, y.ac, reverse = True))
  #sorted(rank_list, key = lambda x:x.ac, reverse = True)
@task
def update_running_contest_rank():
  try:
    contests = Contest.objects.filter(status="running")
  except:
    return
  if not contests:
    return
  for contest in contests:
    update_rank_list(str(contest.contestID))

@task
def update_rank_list(contestID):
  contest_submit_list = ContestSubmit.objects.filter(contestID=contestID).order_by('id')
  rank_list = {}
  FB = {}
  contest = Contest.objects.get(contestID = contestID)
  problem_list = contest.problemList.split(',')
  for p in problem_list:
    FB[(int(p))] = 0

  for contest_submit in contest_submit_list:
    userID = contest_submit.userID
    status = contest_submit.status
    problemID = contest_submit.problemID
    date = contest_submit.date
    time = contest_submit.timestamp
    runID = contest_submit.id
    if not userID in rank_list:
      rank_list[userID] = Rank(userID, contestID)
      for p in problem_list:
        rank_list[userID].problem_list[int(p)] = Rank.Problem(int(p))
    rank_list[userID].problem_list[problemID].add_submit(Rank.Problem.Submit(runID = str(runID),
                                                                             status=status,
                                                                             date_time=str(date) + " " + str(time)))
  #to get if the submit is FB
    if contest_submit.status == "Accepted":
      if FB[problemID] == 0:
        FB[problemID] = 1
        rank_list[userID].problem_list[problemID].FB = 1

  sort_rank(rank_list, contestID, FB)
  contest_rank_list = rank_pb2.ContestRankList()
  contest_rank_list.contestID = contestID
  for userID in rank_list:
    rank = rank_list[userID]
    rank_proto = contest_rank_list.rank.add()
    rank.load_data_to_proto(rank_proto)
  ssdb_api.SetContestRankListProto(contestID, contest_rank_list.SerializeToString())
  '''try:
    contest_rank = ContestRankList.objects.get(contestID=contestID)
  except:
    contest_rank = ContestRankList(contestID=contestID, rank_list_proto_str="")
  contest_rank.rank_list_proto_str = contest_rank_list.SerializeToString()
  print "proto_buffer" + contest_rank.rank_list_proto_str
  contest_rank.save()'''

if __name__ == "__main__":
  update_rank_list(1)
