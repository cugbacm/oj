#!/usr/bin/env python
import sys 
from datetime import *
import time
from django.shortcuts import render
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def contest(request, contest_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
    contest = Contest.objects.get(contestID = contest_id)
    problemList = contest.problemList.split(',')
    problems = Problem.objects.filter(problemID__in = problemList)
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
      return render(request,
                    'cugbacm/contest.html',
                    {
                      'problems': problems,
                      'userID':request.session["userID"],
                      'contest': contest
                    })
  except:
    return HttpResponseRedirect("/index/login")
