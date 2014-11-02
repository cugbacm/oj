#!/usr/bin/env python
import sys 
from datetime import *
import time
from django.shortcuts import render
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit, UserContestMap
from django.http import HttpResponse, HttpResponseRedirect

def contest(request, contest_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")

  contest = Contest.objects.get(contestID = contest_id)
  if str(contest.status) == 'pending':
    return HttpResponse("Sorry, The contest is not start!")

  try: 
    userID_contestID = UserContestMap.objects.get(userID=str(user.userID), contestID=int(contest_id))
  except:
    return HttpResponse("Sorry, " + str(user.userID) + " is not in this contest!")

  problemList = contest.problemList.split(',')
  problems = Problem.objects.filter(problemID__in = problemList)
  problem_ac_count = {}
  problem_all_count = {}
  for problem in problems:

    contest_submits = ContestSubmit.objects.filter(contestID = str(contest_id), problemID = str(problem.problemID))
    problem_all_count[problem.problemID] = len(contest_submits)
    problem.totalSubmission = len(contest_submits) 
    problem_ac_count[problem.problemID] = len(contest_submits.filter(status = "Accepted"))
    problem.ac = len(contest_submits.filter(status = "Accepted"))
  if request.method == 'POST':
    problemID = request.POST['problemID']
    problemTitle = request.POST['problemTitle']
    problemAuthor = request.POST['problemAuthor']
    try:
      if problemID.strip():
        problems = problems.filter(problemID__contains = problemID)
      if problemTitle.strip():
        problems = problems.filter(title__contains = problemTitle)
      if problemAuthor.strip():
        problems = problems.filter(author__contains = problemAuthor)
      return render(
        request, 
        'cugbacm/contest.html', 
        {
          'contest': contest,
          'problems': problems, 
          'problem_ac_count': problem_ac_count,
          'problem_all_count': problem_all_count,
          'userID': request.session["userID"],
          'problemID': problemID,
          'problemTitle': problemTitle,
          'problemAuthor': problemAuthor
        }
      )
    except:
      return render(request,
                    'cugbacm/contest.html',
                    {
                      'problems': {},
                      'userID':request.session["userID"],
                      'contest': contest
                    })
  else:
    #contestants = contest.userList.split(',')
    #if userID in contestants:
    #return HttpResponse("fuck") 
    return render(request,
                  'cugbacm/contest.html',
                  {
                    'problems': problems,
                    'problem_ac_count': problem_ac_count,
                    'problem_all_count': problem_all_count,
                    'userID':request.session["userID"],
                    'contest': contest
                  })
