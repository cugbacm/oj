from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from cugbacm.models import ContestXls, User

class UploadForm(forms.Form):
  contestID = forms.IntegerField(
      widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contest ID'})
      )
  xlsAddr = forms.FileField(
      widget=forms.FileInput(attrs={'value':'Select File'})
      )

def manager(request):
  try:
    user = User.objects.get(userID = request.session['userID'])
  except:
    return HttpResponseRedirect("/index/login")
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
  if user.userID != "QQ":
    return HttpResponse('you are not permited!')

  return render(request, 'cugbacm/manager.html',{'uf':uf, 'userID':request.session['userID']})
