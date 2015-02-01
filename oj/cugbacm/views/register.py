#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect
import hashlib

@csrf_exempt
def encrypt(userID, password):
  first_md5 = hashlib.md5()
  first_md5.update(str(password))
  salt = first_md5.hexdigest()
  second_md5 = hashlib.md5()
  second_md5.update(str(userID) + salt)
  return second_md5.hexdigest()

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
    if len(userID) == 0:
      return HttpResponse("The length of userID should not less than 6.")
    if len(password) < 6:
      return HttpResponse("The length of password should not less than 6.")
    if len(session) == 0:
      return HttpResponse("Please fill session bar.")
    if len(specialty) == 0:
      return HttpResponse("Please fill specialty bar.")
    if len(tel) == 0:
      return HttpResponse("Please fill tel bar.")
    if len(email) == 0:
      return HttpResponse("Please fill email bar.")
    if len(nickname) == 0:
      return HttpResponse("Please fill nickname bar.")
    try:
      user = User.objects.get(userID = userID)
      return HttpResponse("User already existed")
    except:
      password = encrypt(userID, password)
      User(
        userID = userID,
        password = password,
        session = session,
        specialty = specialty,
        tel = tel,
        email = email,
        nickname = nickname).save()
      request.session['userID'] = userID
      return HttpResponse("success")
  else:
    return render(request, 'cugbacm/register.html', {})
