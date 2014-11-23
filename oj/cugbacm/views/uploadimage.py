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

def uploadimage(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")

  if request.method == 'POST':
    p_Id = request.POST['p_Id']
    #form = MyFile(request.POST, request.FILES)
    #if form.is_valid():
    try:
      images = request.FILES.getlist('image')
      for i in images:
        handle_uploaded_image(i, p_Id)
    except:
      pass
    #return HttpResponse("OK_The file is avalueable!!!")
    return HttpResponseRedirect("/index/problemList")
  else:
    return render(request, 'cugbacm/uploadimage.html', {})

#upload image to media/problemID
def handle_uploaded_image(i, name):
  image_name = ""

  try:
    path = "/home/cugbacm/oj/oj/media/images/" + name
    if not os.path.exists(path):
      os.makedirs(path)
    image_name = path + '/' + i.name
    destination = open(image_name, 'wb+')
    for chunk in i.chunks():
      destination.write(chunk)
    destination.close()
    return HttpResponse(path)
  except Exception, e:
    print e

  return image_name
