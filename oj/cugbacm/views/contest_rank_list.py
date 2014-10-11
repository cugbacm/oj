#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit, Contestant
from django.http import HttpResponse, HttpResponseRedirect

def contestRankList(request, contest_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
    # todo: get rank_list
    contest_rank_list = Contestant.objects.filter(contestID = contest_id).order_by('-penalty')
    return render(request,
                 'cugbacm/contestRankList.html',
                 {
                    'userID':request.session['userID'],
                    'contest': Contest.objects.get(contestID = contest_id),
                    'contest_rank_list':contest_rank_list, 
    })
  except: 
    return render(request,
                 'cugbacm/contestRankList.html',
                 {
                    'userID':request.session['userID'],
                    'contest': Contest.objects.get(contestID = contest_id)
                 })
    return HttpResponseRedirect("/index/login")

