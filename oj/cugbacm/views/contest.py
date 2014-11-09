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

  problemList = contest.problemList.split(',')
  problems = Problem.objects.filter(problemID__in = problemList)
  problem_ac_count = {}
  problem_all_count = {}
  problemName = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J'}
  #problemName = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
  for problem in problems:

    contest_submits = ContestSubmit.objects.filter(contestID = str(contest_id), problemID = str(problem.problemID))
    problem_all_count[problem.problemID] = len(contest_submits)
    problem.totalSubmission = len(contest_submits)
    problem_ac_count[problem.problemID] = len(contest_submits.filter(status = "Accepted"))
    problem.ac = len(contest_submits.filter(status = "Accepted"))
  problem_list = []
  count = 0
  for problem in problems:
    ac = False
    no_pass = False
    other = True

    # ac
    try:
      submit = ContestSubmit.objects.filter(contestID = contest_id, problemID = problem.problemID, userID = user.userID)
      for _submit in submit:
        if _submit.status == "Accepted":
          ac = True
      if not ac:
        if len(submit) > 0:
          no_pass = True
    except:
      pass

    status = "other"
    if ac:
      status = "ac"
    if no_pass:
      status = "no_pass"

    problem_list.append([chr(ord('A') + count), problem, status])
    count += 1
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
          'problemAuthor': problemAuthor,
          'problemName': problemName,
          'problem_list': problem_list
        }
      )
    except:
      return render(request,
                    'cugbacm/contest.html',
                    {
                      'problems': {},
                      'userID':request.session["userID"],
                      'contest': contest,
                      'problemName': problemName,
                      'problem_list': problem_list
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
                    'contest': contest,
                    'problemName': problemName,
                    'problem_list': problem_list
                  })
