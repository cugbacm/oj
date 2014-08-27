#!/usr/bin/env python
from datetime import *
import time
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def submitList(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
    submits = Submit.objects.all().order_by('-id')
    if request.method == 'POST':
      userIDSearch = request.POST['userIDSearch']
      problemIDSearch = request.POST['problemIDSearch']
      resultSearch = request.POST['resultSearch']
      languageSearch = request.POST['languageSearch']
      try:
        if userIDSearch.strip():
          submits = submits.filter(userID__contains = userIDSearch)
        if problemIDSearch.strip():
          submits = submits.filter(problemID__contains = problemIDSearch)
        if resultSearch != "Result":
          submits = submits.filter(status = resultSearch)
        if languageSearch != "Language":
          submits = submits.filter(language = languageSearch)

        return render(
          request, 
          'cugbacm/submitList.html',
          {
            'submits': submits, 
            'userID':request.session['userID'],
            'userIDSearch': request.POST['userIDSearch'],
            'problemIDSearch': request.POST['problemIDSearch'],
            'resultSearch': request.POST['resultSearch'],
            'languageSearch': request.POST['languageSearch']
          }
        )
      except:
        return render(request, 'cugbacm/submitList.html', {'submits': {}, 'userID':request.session['userID'] })
    else:
      return render(request, 'cugbacm/submitList.html', {'submits': submits, 'userID':request.session['userID'] })
  except:
    return HttpResponseRedirect("/index/login")

