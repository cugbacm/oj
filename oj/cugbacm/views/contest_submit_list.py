#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def contestSubmitList(request, contest_id):
  results = ("Result","Accepted", "Time Limit Exceeded","Memory Limit Exceeded","Wrong Answer","Runtime Error","Compile Error","Presentation Error","System Error")
  languages = ("Language","g++","gcc","java","python2","python3")
  try:
    user = User.objects.get(userID = request.session['userID'])
    try:
      contest_submits = ContestSubmit.objects.filter(contestID = str(contest_id)).order_by('-runID')
    except:
      contest_submits = ContestSubmit.objects.all()
    contest = Contest.objects.get(contestID = contest_id)
    problemList = contest.problemList.split(',')
    problems = Problem.objects.filter(problemID__in = problemList)
    contest_submit_list = []
    for contest_submit in contest_submits:
      count = 0
      countp = 0
      for problem in problems:
        if problem.problemID == contest_submit.problemID:
          count = countp
        else:
          countp += 1
      contest_submit_list.append([chr(ord('A') + count), contest_submit])
#todo
#ssdb key = contest_id + "\t" + problem_id   value = chr('A') + count
    #return HttpResponse(contest_submit_list)
    if request.method == 'POST':
      userIDSearch = request.POST['userIDSearch']
      problemIDSearch = request.POST['problemIDSearch']
      resultSearch = request.POST['resultSearch']
      languageSearch = request.POST['languageSearch']
      try:
        if userIDSearch.strip():
          contest_submits = contest_submits.filter(userID__contains = userIDSearch)
        if problemIDSearch.strip():
          contest_submits = contest_submits.filter(problemID__contains = problemIDSearch)
        if resultSearch != "Result":
          contest_submits = contest_submits.filter(status = resultSearch)
        if languageSearch != "Language":
          contest_submits = contest_submits.filter(language = languageSearch)

        return render(request,
                      'cugbacm/contestSubmitList.html',
                      {
                        'contest_submit_list':contest_submit_list,
                        'submits': contest_submits,
                        'contest': Contest.objects.get(contestID = contest_id),
                        'userID':request.session['userID'],
                        'userIDSearch': request.POST['userIDSearch'],
                        'problemIDSearch': request.POST['problemIDSearch'],
                        'resultSearch': request.POST['resultSearch'],
                        'languageSearch': request.POST['languageSearch'],
                        'languages':languages,
                        'results':results
                        })
      except:
        return render(request,
                      'cugbacm/contestSubmitList.html',
                      {
                        'submits': {},
                        'contest_submit_list':{},
                        'userID':request.session['userID'],
                        'contest': Contest.objects.get(contestID = contest_id),
                        'results':results,
                        'languages':languages
                      })
    else:
      return render(request,
                    'cugbacm/contestSubmitList.html',
                    {
                      'contest_submit_list':contest_submit_list,
                      'submits': contest_submits,
                      'userID':request.session['userID'],
                      'contest': Contest.objects.get(contestID = contest_id),
                      'results':results,
                      'languages':languages
                    })
  except:
    return HttpResponseRedirect("/index/login")

