#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def contestSubmitList(request, contest_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
    try:
      contest_submits = ContestSubmit.objects.filter(contestID = str(contest_id)).order_by('-runID')
    except:
      contest_submits = ContestSubmit.objects.all()
    #return HttpResponse("fuck")
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
                        'submits': contest_submits,
                        'contest': Contest.objects.get(contestID = contest_id),
                        'userID':request.session['userID'],
                        'userIDSearch': request.POST['userIDSearch'],
                        'problemIDSearch': request.POST['problemIDSearch'],
                        'resultSearch': request.POST['resultSearch'],
                        'languageSearch': request.POST['languageSearch']
                      })
      except:
        return render(request,
                      'cugbacm/contestSubmitList.html',
                      {
                        'submits': {},
                        'userID':request.session['userID'],
                        'contest': Contest.objects.get(contestID = contest_id)
                      })
    else:
      return render(request,
                    'cugbacm/contestSubmitList.html',
                    {
                      'submits': contest_submits,
                      'userID':request.session['userID'],
                      'contest': Contest.objects.get(contestID = contest_id)
                    })
  except:
    return HttpResponseRedirect("/index/login")

