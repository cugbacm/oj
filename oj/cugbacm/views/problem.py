from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from cugbacm.core_hq import main
from cugbacm.core_hq import UserSubmit
from cugbacm.models import User, Submit, Problem, OJAttribute
from celery.task import task
import ssdb_api
from cugbacm.api.judge import Judge
@task
def test(problemID):
  submit = Submit(
    runID = 111,
    userID = "QQ",
    problemID = problemID,
    status = "queueing",
    memory = 10000,
    runTime = 1000,
    codeLength = 100,
    language = 'g++',
    code = "fuck you")
  submit.save()
  Judge(submit)

def problem(request, problem_id):
  languages = ("g++","gcc","java","python2","python3")
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")
  oj_attribute = OJAttribute.objects.all()[0]
  problem = Problem.objects.get(problemID=problem_id)
  user = User.objects.get(userID = request.session['userID'])
  submits = Submit.objects.filter(problemID = problem_id, userID = user.userID).order_by('-id')
  if request.method == 'POST':
    code = request.POST['code']
    language = request.POST['language']
    for i in range(1):
      submit = Submit(
        runID = 111,
        userID = request.session["userID"],
        problemID = problem_id,
        status = "queueing",
        memory = 10000,
        runTime = 1000,
        codeLength = 100,
        language = language,
        code = code)
      submit.save()
      Judge.delay(submit)
    return HttpResponseRedirect("/index/problem/" + str(problem_id) + "?show_submit=true")
  else:
    show_submit = request.GET.get('show_submit')
    if problem.visible == False:
      return HttpResponseRedirect("/index/problemList/")
    try:
      submit = Submit.objects.get(id = request.GET.get('submit'))
      if submit.userID == user.userID and str(submit.problemID) == str(problem_id):
        return render(request,
                      'cugbacm/problem.html',
                      {
                        'problem': problem,
                        'userID': user.userID,
                        'submit': submit,
                        'submits': submits,
                        'languages': languages,
                        'show_submit': show_submit,
                        'oj_attribute': oj_attribute,
                      }
                      )
      else:
        return HttpResponseRedirect("/index/problem/" + str(problem_id))
    except:
      return render(request,
                    'cugbacm/problem.html',
                    {
                      'problem': problem,
                      'userID': user.userID,
                      'submits': submits,
                      'languages': languages,
                      'show_submit': show_submit,
                      'oj_attribute': oj_attribute,
                    }
                    )


