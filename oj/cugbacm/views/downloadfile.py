from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from cugbacm.models import ContestXls

def downloadfile(request, contest_id):
  contest = ContestXls.objects.get(contestID = contest_id)
  filename = str(contest.xlsAddr)
  f = open(filename)
  data = f.read()
  f.close()
  response = HttpResponse(data,mimetype='application/octet-stream')
  response['Content-Disposition']='attachment; filename=%s' % filename
  return response
