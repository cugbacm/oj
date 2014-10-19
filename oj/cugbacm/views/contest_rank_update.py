#!/usr/bin/env python
from datetime import *
import time
import datetime
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit, ContestRankList
from cugbacm.proto import rank_pb2
from celery.task import task
#import ssdb_api
class Rank():
  class Problem():
    class Submit():
      def __init__(self, status="", date_time=datetime.datetime.now()):
        self.status = status
        self.date_time = date_time

    def __init__(self, problemID):
      self.problemID = problemID
      self.submit_list = []

    def add_submit(self, submit):
      self.submit_list.append(submit)

  def __init__(self, userID, contestID):
    self.userID = userID
    self.contestID = contestID
    self.problem_list = {}
    self.ac = 0
    self.penalty = 0

  def load_data_to_proto(self):
    rank = rank_pb2.Rank()
    rank.userID = self.userID
    rank.contestID = self.contestID
    rank.ac = self.ac
    rank.penalty = self.penalty

    for problemID in self.problem_list:
      problem = self.problem_list[problemID]
      p = rank.problem.add()
      p.problemID = problem.problemID
      for submit in problem.submit_list:
        s = p.submit.add()
        s.status = submit.status
        s.date_time = "2014 10 10 10 10 10"
        #s.date_time = time.strftime(submit.date_time, '%Y %m %d %H %M %S')
    return rank
def sort_rank(rank_list):
  for userID in rank_list:
    rank = rank_list[userID]
    for problem in rank.problem_list:
      flag = 0
      for submit in rank.problem_list[problem].submit_list:
        if submit.status == "Accepted" and flag == 0:
          rank.ac = rank.ac + 1
          flag = 1
          rank.penalty = rank.penalty + 104
        elif not submit.status == "Accepted":
          rank.penalty = rank.penalty + 20

  #rank_list = sorted(rank_list, cmp = lambda x,y:cmp(x.ac, y.ac)) or cmp(x.penalty, y.penalty))

@task
def update_rank_list(contestID):
  contest_submit_list = ContestSubmit.objects.filter(contestID=contestID)
  rank_list = {}

  for contest_submit in contest_submit_list:
    userID = contest_submit.userID
    status = contest_submit.status
    problemID = contest_submit.problemID
    date_time = contest_submit.timestamp
    if not userID in rank_list:
      rank_list[userID] = Rank(userID, contestID)
    if not problemID in rank_list[userID].problem_list:
      rank_list[userID].problem_list[problemID] = Rank.Problem(problemID)
    rank_list[userID].problem_list[problemID].add_submit(Rank.Problem.Submit(status=status, date_time=date_time))

  sort_rank(rank_list)
  contest_rank_list = rank_pb2.ContestRankList()
  contest_rank_list.contestID = contestID
  for userID in rank_list:
    rank = rank_list[userID]
    rank_proto = contest_rank_list.rank.add()
    rank_proto = rank.load_data_to_proto()
  #ssdb_api.SetContestRankListProto(contestID, contest_rank_list.SerializeToString())
  try:
    contest_rank = ContestRankList.objects.get(contestID=contestID)
  except:
    contest_rank = ContestRankList(contestID=contestID, rank_list_proto_str="")
  contest_rank.rank_list_proto_str = contest_rank_list.SerializeToString()
  contest_rank.save()

if __name__ == "__main__":
  update_rank_list(1)
