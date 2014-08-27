#!/usr/bin/env python
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit
from django.http import HttpResponse, HttpResponseRedirect

def userList(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")
  users = User.objects.all().order_by('-accepted')
  if request.method == 'POST':
    userIDForSearch = request.POST['UserIdForSearchInput']
    nickNameForSearch = request.POST['NickNameForSearchInput']
    try:
      if userIDForSearch.strip():
        users = users.filter(userID__contains = userIDForSearch)
      if nickNameForSearch.strip():
        users = users.filter(nickname__contains = nickNameForSearch)
      return render(request, 'cugbacm/userList.html',{
        'users':users,
        'userID':request.session['userID'],
        'UserIdForSearch':userIDForSearch,
        'NickNameForSearch':nickNameForSearch
      })
    except:
      return render(request,'cugbacm/userList.html', {'users':{},'userID':request.session['userID']})
  else:    
    return render(request, 'cugbacm/userList.html', {'users': users, 'userID':request.session['userID']})

