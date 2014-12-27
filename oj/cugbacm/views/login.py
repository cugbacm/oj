#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect
import hashlib

def encrypt(password):
  m = hashlib.md5()
  m.update(password)
  return m.hexdigest()

@csrf_exempt
def login(request):
  if request.method == 'POST':
    '''userID = request.POST['userID']
    password = request.POST['password']'''
    userID = request.POST['userID']
    password = request.POST['password']
    password = encrypt(password)
    try:
      user = User.objects.get(userID = userID)
      if user.password != password:
        return HttpResponse("password error!")
      else:
        request.session["userID"] = userID
        return HttpResponse("success")
    except:
      return HttpResponse(userID+" does not exsits")
  else:
    login_out = request.GET.get('login_out')
    if login_out == "true":
        del request.session['userID']
    try:
      user = User.objects.get(userID = request.session['userID'])
      return HttpResponseRedirect("/index/problemList")
    except:
      return render(request, 'cugbacm/login.html', {})

