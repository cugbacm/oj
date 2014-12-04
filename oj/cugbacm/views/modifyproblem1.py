#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def modifyproblem1(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")

  if request.method == 'POST':
    if request.POST.has_key("gpd"):
      try:
        pid = request.POST['problem_id']
        problem = Problem.objects.get(problemID = pid)
      except:
        return HttpResponseRedict("/index/manager")

      return render(request, 'cugbacm/manager.html', {"modify":True, "problem":problem})
    else:
      p_Id = request.POST['p_Id']
      problem_title = request.POST['problem_title']
      problem_tlimit = request.POST['problem_tlimit']
      problem_mlimit = request.POST['problem_mlimit']
      problem_des = request.POST['problem_des']
      problem_input = request.POST['problem_input']
      problem_output = request.POST['problem_output']
      problem_sinput = request.POST['problem_sinput']
      problem_soutput = request.POST['problem_soutput']
      problem_hint = request.POST['problem_hint']
      problem_visible = request.POST['problem_visible']
      problem_author = request.POST['problem_author']
      problem = Problem(
        problemID = p_Id,
        title = problem_title,
        timeLimit = problem_tlimit,
        memoryLimit = problem_mlimit,
        ac = 0,
        wa = 0,
        tle = 0,
        mle = 0,
        pe = 0,
        ce = 0,
        se = 0,
        totalSubmission = 0,
        description = problem_des,
        input = problem_input,
        output = problem_output,
        sampleInput = problem_sinput,
        sampleOutput = problem_soutput,
        hint = problem_hint,
        visible = problem_visible,
        author = problem_author,
      )
      #return HttpResponse('upload ok!')
      problem.save()
      return HttpResponseRedirect("/index/problemList")
  else:
    try:
      problem = Problem.objects.get(problemID = problem_id)
    except:
      return HttpResponseRedict("/index/manager")

    return render(request, 'cugbacm/manager.html', {"modify":True, "problem":problem})
