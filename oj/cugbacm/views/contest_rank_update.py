#!/usr/bin/env python
from datetime import *
import time
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit

class Rank(object):
  class Problem(object):
    class Submit(object):
      def __init__(self, status="", date_time=datetime.now()):
        self.status = status
        self.data_time = date_time

    def __init__(self, problemID):
      self.problemID = problemID
      self.commit_list = []

    def add_submit(self, submit):
      self.commit_list.append(submit)

  def __init__(self, userID, contestID):
    self.userID = userID
    self.contestID = contestID
    self.problem_list = {}
    self.ac = 0
    self.penalty = 0

def sort_rank(rank_list):
  for userID in rank_list:
    rank = rank_list[userID]
    for problem in rank.problem_list:
      flag = 0
      for submit in rank.problem_list[problem].commit_list:
        if submit.status == "Accepted" and flag == 0:
          rank.ac = rank.ac + 1
          flag = 1
          rank.penalty = rank.penalty + submit.data_time
        elif not submit.status == "Accepted":
          rank.penalty = rank.penalty + 20

  rank_list_result = sorted(rank_list, cmp = lambda x,y:cmp(x.ac, y.ac) or cmp(x.penalty, y.penalty))

def update_rank_list(contestID):
  contest_submit_list = ContestSubmit.object.filter(contestID=contestID)
  rank_list = {}

  for contest_submit in contest_submit_list:
    userID = contest_submit.userID
    status = contest_submit.status
    problemID = contest_submit.problemID
    date_time = datetime.fromtimestamp(contest_submit.timestamp)
    if not userID in rank_list:
      rank_list[userID] = Rank(userID, contestID)
    if not problemID in rank_list[userID].problem_list:
      rank_list[userID].problem_list[problemID] = Rank.Problem(problemID)
    rank_list[userID].problem_list[problemID].add_submit(Rank.Problem.Submit(status, data_time))

  sort_rank(rank_list)
  
  
