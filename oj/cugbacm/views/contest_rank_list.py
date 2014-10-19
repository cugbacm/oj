#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit, ContestRankList
import cugbacm.proto.rank_pb2
from django.http import HttpResponse, HttpResponseRedirect
from cugbacm.views.contest_rank_update import update_rank_list
def contestRankList(request, contest_id):
  update_rank_list(contest_id)
  try:
    user = User.objects.get(userID = request.session['userID'])
    # todo: get rank_list
    try:
      contest_rank_list = ContestRankList.objects.filter(contestID=contest_id)
    except:
      contest_rank_list = ContestRankList(contestID=contest_id, rank_list_proto_str="")
    rank_list = rank_pb2.ContestRankList()
    rank_list.ParseFromString(contest_rank_list.rank_list_proto_str)
    return render(request,
                 'cugbacm/contestRankList.html',
                 {
                    'userID':request.session['userID'],
                    'contest': Contest.objects.get(contestID = contest_id),
                    'rank_list':rank_list,
    })
  except:
    return render(request,
                 'cugbacm/contestRankList.html',
                 {
                    'userID':request.session['userID'],
                    'contest': Contest.objects.get(contestID = contest_id)
                 })
    return HttpResponseRedirect("/index/login")

