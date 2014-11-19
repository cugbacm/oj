from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from cugbacm.models import ContestXls

class UploadForm(forms.Form):
  contestID = forms.IntegerField()
  xlsAddr = forms.FileField()

def manager(request):
  if request.method == "POST":
    uf = UploadForm(request.POST,request.FILES)
    if uf.is_valid():
      contestID = uf.cleaned_data['contestID']
      xlsAddr = uf.cleaned_data['xlsAddr']
      cx = ContestXls()
      cx.contestID = contestID
      cx.xlsAddr = xlsAddr
      cx.save()
      return HttpResponse('upload ok!')
  else:
    uf = UploadForm()
  return render(request, 'cugbacm/manager.html',{'uf':uf})
