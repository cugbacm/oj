#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit,Contestant
from django.http import HttpResponse, HttpResponseRedirect

@csrf_exempt
def login(request):
  if request.method == 'POST':

    '''userID = request.POST['userID']
    password = request.POST['password']'''
    userID = request.POST['userID']
    password = request.POST['password']
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
    try: 
      del request.session['userID'] 
    except:
      pass
    return render(request, 'cugbacm/login.html', {})

