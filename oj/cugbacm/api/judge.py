from cugbacm.core_hq import main
from cugbacm.core_hq import UserSubmit
from celery.task import task
from cugbacm.models import User, Submit, Problem, OJAttribute
import cugbacm.views.ssdb_api

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
  print submit.status, submit.runTime, submit.memory


  ssdb_api.InsertUserProblemStatus(user.userID, submit.problemID, submit.status)

  if submit.status == "Accepted":
    if Submit.objects.filter(userID = user.userID, problemID = submit.problemID, status = "Accepted").count() == 1:
      user.accepted = user.accepted + 1
      if user.acList == None:
        user.acList = ""
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
