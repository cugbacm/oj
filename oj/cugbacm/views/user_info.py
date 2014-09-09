#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def userInfo(request, user_id):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")
  other = User.objects.get(userID = user_id)
  if request.method == 'POST':
    if request.POST.has_key("Modify"):
      userID = request.session['userID']
      oldPassword = request.POST['oldPassword']
      password = request.POST['password']
      confirmPassword = request.POST['confirmPassword']
      session = request.POST['session']
      specialty = request.POST['specialty']
      tel = request.POST['tel']
      email = request.POST['email']
      nickname = request.POST['nickname']
      if oldPassword != user.password:
        return HttpResponse("password error")
      else:
        user.password = oldPassword
        user.session = session
        user.specialty = specialty
        user.tel = tel
        user.email = email
        user.nickname = nickname
        if password.strip() != '' and password == confirmPassword:
          user.password = password
          user.save()
          other = User.objects.get(userID = user_id)
          return render(request, 'cugbacm/userInfo.html', {'userID':request.session['userID'],'user': user, 'other':other, 'id':user_id})
        else:
          if password != confirmPassword:
            return HttpResponse("password and confirmPassword is not the same!")
          else:
            user.save()
            other = User.objects.get(userID = user_id)
            return render(request, 'cugbacm/userInfo.html', {'userID':request.session['userID'], 'user':user, 'other':other, 'id':user_id})
    else:
      curproblemList = []
      if user.acList != None:
        curproblemList = user.acList.split(',')
      otherproblemList = []
      if other.acList != None:
        otherproblemList = other.acList.split(',')
      curproblemList.sort()
      otherproblemList.sort()
      bothAccepted = search_same(curproblemList, otherproblemList)
      onlyAAccepted = curproblemList
      onlyBAccepted = otherproblemList
      return render(request, 'cugbacm/userInfo.html', {'bothAccepted':bothAccepted,'onlyAAccepted':onlyAAccepted,'onlyBAccepted':onlyBAccepted,'userID':request.session['userID'],'user': user, 'other':other, 'id':user_id,'compare':1 })  
  else:
    return render(request, 'cugbacm/userInfo.html', {'userID':request.session['userID'],'user': user, 'other':other, 'id':user_id })
    

def search_same(A,B):
  AB = []
  start = 0
  len_B = len(B)
  for x in A:
    for i in range(start,len_B):
      y = B[i]
      if x == y:
        AB.append(x)
        len_b = len(B)
      elif x < y:
        start = i
  
  for x in AB:
    A.remove(x)
  for y in AB:
    B.remove(y)
  return AB

