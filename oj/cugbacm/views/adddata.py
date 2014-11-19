#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
import os
class MyFile(forms.Form):
  title = forms.CharField(max_length=50)
  file = forms.FileField()

def adddata(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")

  if request.method == 'POST':
    p_Id = request.POST['p_Id']
    #form = MyFile(request.POST, request.FILES)
    #if form.is_valid():
    files = request.FILES.getlist('file')
    for f in files:
      handle_uploaded_file(f, p_Id)
    #return HttpResponse("OK_The file is avalueable!!!")
    return HttpResponseRedirect("/index/problemList")
  else:
    return render(request, 'cugbacm/adddata.html', {})


def handle_uploaded_file(f, name):
  file_name = ""
  
  try:
    path = "/home/cugbacm/Documents/data_dir/" + name
    if not os.path.exists(path):
      os.makedirs(path)
    file_name = path + '/' + f.name
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
      destination.write(chunk)
    destination.close()
    return HttpResponse(path)
  except Exception, e:
    print e
  
  return file_name
