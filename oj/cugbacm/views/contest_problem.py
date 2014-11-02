#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect
from celery.task import task
from cugbacm.core_hq import main
from cugbacm.core_hq import UserSubmit
from cugbacm.views.contest_rank_update import update_rank_list
from cugbacm.proto import contestant_ac_pb2
@task
def Judge(contestsubmit):
  problem = Problem.objects.get(problemID = contestsubmit.problemID)
  user = User.objects.get(userID = contestsubmit.userID)
  user_submit = UserSubmit(
    solution_id = contestsubmit.id,
    problem_id = contestsubmit.problemID,
    language = contestsubmit.language,
    user_id = contestsubmit.userID,
    program = contestsubmit.code,
    mem_limit = problem.memoryLimit,
    time_limit = problem.timeLimit
  )
  result = main(user_submit)
  if "result" in result:
    contestsubmit.status = result['result']
  if "codeLength" in result:
    contestsubmit.codeLength = result['codeLength']
  if "take_time" in result:
    contestsubmit.runTime = result['take_time']
  if "take_memeory" in result:
    contestsubmit.memory = result['take_memory']
  contestsubmit.save()
  print contestsubmit.status

  if contestsubmit.status == "Accepted":
    if ContestSubmit.objects.filter(contestID = contestsubmit.contestID, userID = user.userID, problemID = contestsubmit.problemID, status = "Accepted").count() == 1:
      user.accepted = user.accepted + 1
      if user.acList == None:
        user.acList = ""
      user.acList += str(contestsubmit.problemID) + ","
    problem.ac = problem.ac + 1
  elif contestsubmit.status == "Time Limit Exceeded":
    problem.tle = problem.tle + 1
  elif contestsubmit.status == "Memory Limit Exceeded":
    problem.mle = problem.mle + 1
  elif contestsubmit.status == "Wrong Answer":
    problem.wa = problem.wa + 1
  elif contestsubmit.status == "Runtime Error":
    problem.re = problem.re + 1
  elif contestsubmit.status == "Compile Error":
    problem.ce = problem.ce + 1
  elif contestsubmit.status == "Presentation Error":
    problem.pe = problem.pe + 1
  elif contestsubmit.status == "System Error":
    problem.se = problem.se + 1

  problem.totalSubmission = problem.totalSubmission + 1
  user.total = user.total + 1
  user.save()
  problem.save()
  return contestsubmit.status

def contestProblem(request, contest_id, problem_id):
  languages = ("g++", "gcc", "java", "python2", "python3")
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect('/index/login')
  problem = Problem.objects.get(problemID = problem_id)
  submits  = ContestSubmit.objects.filter(contestID = contest_id, problemID = problem_id, userID = user.userID).order_by("-id")
  if request.method == 'POST':
    code = request.POST['code']
    language = request.POST['language']
    for i in range(1):
      contestsubmit = ContestSubmit(
        runID = 111,
        userID = request.session["userID"],
        problemID = problem_id,
        status = "queueing",
        memory = 10000,
        runTime = 1000,
        codeLength = 100,
        language = language,
        contestID = contest_id,
        code = code)
      contestsubmit.save()
      Judge.delay(contestsubmit)
    return HttpResponseRedirect("/index/contest/" + str(contest_id) + "/problem/" + str(problem_id))
  else:
    show_submit = request.GET.get('show_submit')
    try:
      submit = ContestSubmit.objects.get(id = request.GET.get('submit'))
      if str(submit.userID) == str(user.userID) and str(submit.problemID) == str(problem_id) and str(submit.contestID) == str(contest_id):
        return render(request,
                      'cugbacm/contestProblem.html',
                      {
                        'problem': problem,
                        'userID': user.userID,
                        'submit': submit,
                        'submits': submits,
                        'contestID':contest_id,
                        'languages':languages,
                        'show_submit': show_submit,
                      }
                      )
      else:
        return HttpResponseRedirect("/index/contest/" + str(contest_id) + "/problem/" + str(problem_id))
    except:
      return render(request,
                    'cugbacm/contestProblem.html',
                    {
                      'problem': problem,
                      'userID': user.userID,
                      'submits':submits,
                      'contestID':contest_id,
                      'languages':languages,
                      'show_submit': show_submit,
                    }
                    )



