#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def addproblem(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")

  if request.method == 'POST':

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


    try:
      problem = Problem.objects.get(problemID = p_Id)
      problem.problemID = p_Id
      problem.title = problem_title
      problem.timeLimit = problem_tlimit
      problem.memoryLimit = problem_mlimit
      problem.ac = 0
      problem.wa = 0
      problem.tle = 0
      problem.mle = 0
      problem.pe = 0
      problem.ce = 0
      problem.se = 0
      problem.totalSubmission = 0
      problem.description = problem_des
      problem.input = problem_input
      problem.output = problem_output
      problem.sampleInput = problem_sinput
      problem.sampleOutput = problem_soutput
      problem.hint = problem_hint
      problem.visible = problem_visible
      problem.author = problem_author
    except:
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
    return render(request, 'cugbacm/addproblem.html', {"modify":False})
