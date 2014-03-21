from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit
from django.http import HttpResponse
import pika
import CompileCpp
import send
from cugbacm.forms import UserRegisterForm, SubmitForm
# Create your views here.

def submit(request):
	form = SubmitForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			runID = form.cleaned_data['runID']
			userID = form.cleaned_data['userID']
			problemID = form.cleaned_data['problemID']
			status = form.cleaned_data['status']
			memory = form.cleaned_data['memory']
			time = form.cleaned_data['time']
			codeLength = form.cleaned_data['codeLength']
			date = form.cleaned_data['date']
			timestamp = form.cleaned_data['timestamp']
			code = form.cleaned_data['code']
			Submit(
				runID = runID, 
				userID = userID,
				problemID = problemID,
				status = "queueing",
				memory = memory,
				time = time,
				codeLength = codeLength,
				date = date,
				timestamp = timestamp,
				code = code).save()
			sendRunID(runID)
			#status = CompileCpp.main('1000', 'c++', code)
			return HttpResponse(runID)
	else:
		return render(request, 'cugbacm/submit.html', {'form': form})
		
def register(request):
	form = UserRegisterForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			name = form.cleaned_data['name']
			password = form.cleaned_data['password']
			session = form.cleaned_data['session']
			specialty = form.cleaned_data['specialty']
			tel = form.cleaned_data['tel']
			email = form.cleaned_data['email']
			nickname = form.cleaned_data['nickname']
			User(
				name = name, 
				password = password,
				session = session,
				specialty = specialty,
				tel = tel,
				email = email,
				nickname = nickname).save()
			return HttpResponse("register success!")
	else:
		return render(request, 'cugbacm/register.html', {'form': form})
