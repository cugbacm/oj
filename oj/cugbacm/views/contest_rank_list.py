#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from cugbacm.proto import rank_pb2
from django.http import HttpResponse, HttpResponseRedirect
from cugbacm.views.contest_rank_update import update_rank_list, Rank
import ssdb_api

def ac(s):
  return s['ac']

def penalty(s):
  return s['penalty']

def contestRankList(request, contest_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")
    # todo: get rank_list
  update_rank_list(contest_id)
  contest_rank_list = ssdb_api.GetContestRankListProto(contest_id)
  rank_list = rank_pb2.ContestRankList()
  rank_list.ParseFromString(contest_rank_list)
 #return HttpResponse(rank_list)
 #rank_list.ParseFromString(contest_rank_list.rank_list_proto_str.encode("utf-8"))
  rank_list_dic = {}
  ranklist = []
  for rank in rank_list.rank:
    rank_list_dic[rank.userID] = {}
    rank_list_dic[rank.userID]['user_id'] = rank.userID
    rank_list_dic[rank.userID]['ac'] = rank.ac
    rank_list_dic[rank.userID]['penalty'] = (rank.penalty)
    rank_list_dic[rank.userID]['penalty_hms'] = str(rank.penalty/3600) + ":" + str((rank.penalty%3600)/60) + ":" + str((rank.penalty%3600) % 60)
    rank_list_dic[rank.userID]['total'] = rank.total
    for problem_ in rank.problem:
      rank_list_dic[rank.userID][str(problem_.problemID)] = {}
      rank_list_dic[rank.userID][str(problem_.problemID)]['acindex'] = problem_.acindex
      rank_list_dic[rank.userID][str(problem_.problemID)]['totalindex'] = problem_.totalindex
      rank_list_dic[rank.userID][str(problem_.problemID)]['time'] = problem_.time
      rank_list_dic[rank.userID][str(problem_.problemID)]['FB'] = problem_.FB
      rank_list_dic[rank.userID][str(problem_.problemID)]['time_hms'] = str(problem_.time/3600) + ":" + str((problem_.time%3600)/60) +":" + str((problem_.time%3600)%60)
      #for submit_ in problem_.submit:
        #rank_list_dic[rank.userID][str(problem_.problemID)][submit_.runID] = {}
        #rank_list_dic[rank.userID][str(problem_.problemID)][submit_.runID]['status'] = submit_.status
        #rank_list_dic[rank.userID][str(problem_.problemID)][submit_.runID]['date_time'] = submit_.date_time
       # rank_list_dic[rank.userID][problem_.problemID]['date_time'] = submit_.date_time
    ranklist.append(rank_list_dic[rank.userID])

  #ranklist = sorted(ranklist, key = lambda r1:r1['ac'] or r1['penalty'])
  ranklist = sorted(ranklist, key = lambda r:(-r['ac'], r['penalty']))
  #ranklist.reverse()
  #return HttpResponse(ranklist)
  #ranklist.reverse()
  #ranklist = sorted(ranklist, cmp = lambda x,y:cmp(x['ac'], y['ac']), reverse = True or cmp(x['penalty'], y['penalty']))
#to get the problemid from contest
  contest = Contest.objects.get(contestID = contest_id)
  problem_arr = []
  problem_arr = contest.problemList.split(',')
  problemName = []
  count = 0
  for id in problem_arr:
    problemName.append([chr(ord('A')+count), id])
    count += 1

  #return HttpResponse(ranklist)
 #return HttpResponse(rank_list)
  return render(request,
               'cugbacm/contestRankList.html',
               {
                  'userID':request.session['userID'],
                  'contest': Contest.objects.get(contestID = contest_id),
                  'rank_list_dic':rank_list_dic,
                  'problem_arr':problem_arr,
                  'ranklist':ranklist,
                  'problemName':problemName,
  })
