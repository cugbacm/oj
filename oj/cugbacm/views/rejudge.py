from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from cugbacm.core_hq import main
from cugbacm.core_hq import UserSubmit
from cugbacm.models import User, Submit, Problem,ContestSubmit
from celery.task import task


@task
def Judge(submit):
  problem = Problem.objects.get(problemID = submit.problemID)
  user = User.objects.get(userID = submit.userID)
  user_submit = UserSubmit(
    solution_id = submit.id,
    problem_id = submit.problemID,
    language = submit.language,
    user_id = submit.userID,
    program = submit.code,
    mem_limit = problem.memoryLimit,
    time_limit = problem.timeLimit
  )
  result = main(user_submit)
  if "result" in result:
    submit.status = result['result']
  if "codeLength" in result:
    submit.codeLength = result['codeLength']
  if "take_time" in result:
    submit.runTime = result['take_time']
  if "take_memory" in result:
    submit.memory = result['take_memory']
  submit.save()
  print submit.status

  if submit.status == "Accepted":
    if Submit.objects.filter(userID = user.userID, problemID = submit.problemID).count() == 1:
      user.accepted = user.accepted + 1
      if user.acList == None:
          user.acList = ""
   # user.accepted = user.accepted + 1
      user.acList += str(submit.problemID) + ","
    problem.ac = problem.ac + 1
  elif submit.status == "Time Limit Exceeded":
    problem.tle = problem.tle + 1
  elif submit.status == "Memory Limit Exceeded":
    problem.mle = problem.mle + 1
  elif submit.status == "Wrong Answer":
    problem.wa = problem.wa + 1
  elif submit.status == "Runtime Error":
    problem.re = problem.re + 1
  elif submit.status == "Compile Error":
    problem.ce = problem.ce + 1
  elif submit.status == "Presentation Error":
    problem.pe = problem.pe + 1
  elif submit.status == "System Error":
    problem.se = problem.se + 1
  problem.totalSubmission = problem.totalSubmission + 1
  user.total = user.total + 1
  user.save()
  problem.save()
  return submit.status

def rejudge(request,run_id):
  try:
    submit = Submit.objects.get(id = run_id)
    Judge.delay(submit)
    return HttpResponse("rejudged")
  except:
    return HttpResponse("rejudge failed! - no submit found")

def rejudgeRange(request, start_run_id, end_run_id):
  try:
    for i in range(int(start_run_id), int(end_run_id)):
      submit = Submit.objects.get(id = i)
      Judge.delay(submit)
      return HttpResponse("rejudgedRange")
  except:
    return HttpResponse("rejudge failed! - no submit found")
def rejudgeProblem(request, problem_id):
  try:
    submits = Submit.objects.filter(problemID = problem_id)
    for s in submits:
      Judge.delay(s)
    return HttpResponse("rejudged")
  except:
    return HttpResponse("rejudge failed! - no submit found")
def rejudgeContestProblem(request,contest_id, problem_id):
  try:
    submits = ContestSubmit.objects.filter(contestID = contest_id,problemID = problem_id)
    for s in submits:
      Judge.delay(s)
    return HttpResponse("rejudged!")
  except:
    return HttpResponse("rejudge failed! - no submit found")
def rejudgeContest(request, contest_id):
  try:
    submits = ContestSubmit.objects.filter(contestID = contest_id)
    for s in submits:
      Judge.delay(s)
    return HttpResponse("rejudged!")
  except:
    return HttpResponse("rejudge failed! - no submit found")
