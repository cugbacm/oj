#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

@csrf_exempt
def register(request):
  if request.method == 'POST':
    userID = request.POST['userID']
    password = request.POST['password']
    confirmPassword = request.POST['confirmPassword']
    session = request.POST['session']
    specialty = request.POST['specialty']
    tel = request.POST['tel']
    email = request.POST['email']
    nickname = request.POST['nickname']
    if password != confirmPassword:
      return HttpResponse("Password and confirm password must be identical.")
    if len(password) < 6:
      return HttpResponse("The length of password should not less than 10.")
    User(
      userID = userID,
      password = password,
      session = session,
      specialty = specialty,
      tel = tel,
      email = email,
      nickname = nickname).save()
    request.session['userID'] = userID
    return HttpResponseRedirect("/index/problemList")
  else:
    return render(request, 'cugbacm/register.html', {})
