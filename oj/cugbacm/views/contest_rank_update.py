#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def contestRankUpdate(ContestSubmit):
 # try:
 # user = User.objects.get(userID = request.session['userID'])
 # todo: get rank_list
 # contest_submit = ContestSubmit.objects.get(contestID = contest_id)
  user_id = ContestSubmit.userID
  contestant = Contestant.objects.get(userID = user_id)
  problem_id = ContestSubmit.problemID
  contest_problem = Problem.objects.get(problemID = problem_id)
  if ContestSubmit.status == "Accepted":
    contestant.ac = contest_user.ac + 1
    if contestant.acList == None:
      contestant.acList = ""
    contestant.acList += str(ContestSubmit.problemID)+","
    contest_problem.ac = contest_problem.ac + 1
    contestant.penalty = contestant.penalty + "00:00:20"
  elif ContestSubmit.status == "Time Limit Exceeded":
    contest_problem.tle = contest_problem.tle + 1
    contestant.time = contestant.penalty + 20
  elif ContestSubmit.status == "Memory Limit Exceeded":
    contest_problem.mle = contest_problem.mle + 1
    contestant.time = contestant.penalty + 20
  elif ContestSubmit.status == "Wrong Answer":
    contest_problem.wa = contest_problem.wa + 1
    contestant.time = contestant.penalty + 20
  elif ContestSubmit.status == "Runtime Error":
    contesr_problem.re = contest_problem.re + 1
    contestant.time = contestant.penalty + 20
  elif ContestSubmit.status == "Compile Error":
    contest_problem.ce = contest_problem.pe + 1
    contestant.time = contestant.penalty + 20
  elif ContestSubmit.status == "Presentation Error":
    contest_problem.pe = contest_problem.pe + 1
    contestant.time = contestant.penalty + 20
  elif ContestSubmit.status == "System Error":
    contest_problem.se = contest_problem.se + 1
    contestant.time = contestant.penalty + 20
  contest_problem.totalSubmission = contest_problem.totalSubmission + 1
  contestant.total = contest_user.total + 1
  contestant.save()
  contest_problem.save()
    
  contest_rank_list = Contestant.objects.get(contestID = contest_id).order_by('-penalty')
    
   # return render(request,
    #             'cugbacm/contestRankList.html',
     #            {
      #              'userID':request.session['userID'],
       #             'contest': Contest.objects.get(contestID = contest_id)
  #      'contest_rank_list':contest_rank_list
         #        })
  #except:
    
   # return render(request,
    #             'cugbacm/contestRankList.html',
     #            {
      #              'userID':request.session['userID'],
       #             #'contest': Contest.objects.get(contestID = contest_id)
        #         })
   # return HttpResponseRedirect("/index/login")

