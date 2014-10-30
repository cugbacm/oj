#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit, ContestRankList
from cugbacm.proto import rank_pb2
from django.http import HttpResponse, HttpResponseRedirect
from cugbacm.views.contest_rank_update import update_rank_list, Rank
import ssdb_api
def contestRankList(request, contest_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")
    # todo: get rank_list
  rank = Rank("1","zldevil2011")
  #contest_rank_list = ssdb_api.GetContestRankListProto(contest_id)
  #print contest_rank_list
  update_rank_list(contest_id)
  contest_rank_list = ssdb_api.GetContestRankListProto(contest_id)
  rank_list = rank_pb2.ContestRankList()
  rank_list.ParseFromString(contest_rank_list)
  rank_list = {
    'QQ': {
      'ac':1,
      'fuck':'fuck',
    },
    'ZHAOLONG': {
      'ac':2,
      'fuck':'fuck',
    },
  }
  return render(request,
               'cugbacm/contestRankList.html',
               {
                  'userID':request.session['userID'],
                  'contest': Contest.objects.get(contestID = contest_id),
                  'rank_list':rank_list,
  })
