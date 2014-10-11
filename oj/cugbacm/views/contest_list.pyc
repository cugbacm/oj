#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def contestList(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
    contests = Contest.objects.all()
    for contest in contests:
      start_date = contest.startTime
      start_time = contest.startTimestamp
      end_date = contest.endTime
      end_time = contest.endTimestamp
      today = date.today()
      start = datetime(start_date.year,
                       start_date.month,
                       start_date.day,
                       start_time.hour,
                       start_time.minute,
                       start_time.second)
      
      end = datetime(end_date.year,
                     end_date.month,
                     end_date.day,
                     end_time.hour,
                     end_time.minute,
                     end_time.second)
      now = datetime.now()
      if start > now:
        contest.status = "pending"
      elif start <= now and end >= now:
        contest.status = "running"
      else:
        contest.status = "passed"
      contest.save()

    if request.method == 'POST':
      contestID = request.POST['contestID']
      contestTitle = request.POST['contestTitle']
      contestAuthor = request.POST['contestAuthor']
      try:
        if contestID.strip():
          contests = contests.filter(contestID__contains = contestID)
        if contestTitle.strip():
          contests = contests.filter(title__contains = contestTitle)
        if contestAuthor.strip():
          contests = contests.filter(author__contains = contestAuthor)
        return render(
          request, 
          'cugbacm/contestList.html', 
          {
            'contests': contests, 
            'userID': request.session["userID"],
            'contestID': contestID,
            'contestTitle': contestTitle,
            'contestAuthor': contestAuthor
          }
        )
      except:
        return render(request, 'cugbacm/contestList.html', {'contests': {}, 'userID':request.session["userID"]})
    else:
    #return HttpResponse("fuck")
      return render(request, 'cugbacm/contestList.html', {'contests': contests, 'userID':request.session["userID"]})
  except:
    return HttpResponseRedirect("/index/login")
