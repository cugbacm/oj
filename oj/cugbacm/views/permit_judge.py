#!import sys
from datetime import *
import time
from django.shortcuts import render
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit, UserContestMap
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

@csrf_exempt
def permit_judge(request, contest_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")
  if request.method == 'POST':
    contest = Contest.objects.get(contestID = contest_id)
    if contest.public == 1:
      return HttpResponse("success")
    try:
      userID_contestID = UserContestMap.objects.get(userID=str(user.userID), contestID=int(contest_id))
      return HttpResponse("success")
    except:
      return HttpResponse("Sorry,You are not permitted!")

