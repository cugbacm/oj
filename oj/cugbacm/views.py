#!/usr/bin/env python
import pika
import sys
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem
from django.http import HttpResponse
from cugbacm.forms import UserRegisterForm, SubmitForm, ProblemForm
from celery.decorators import task
from CompileCpp import main
# Create your views here.
@task
def Judge(submit):
	submit.status = main('1000', 'c++', submit.code)
	submit.save()
	return submit.status

def submit(request):
	form = SubmitForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			runID = form.cleaned_data['runID']
			userID = form.cleaned_data['userID']
			problemID = form.cleaned_data['problemID']
			status = form.cleaned_data['status']
			memory = form.cleaned_data['memory']
			runTime = form.cleaned_data['runTime']
			codeLength = form.cleaned_data['codeLength']
			date = form.cleaned_data['date']
			timestamp = form.cleaned_data['timestamp']
			code = form.cleaned_data['code']
			submit = Submit(
				runID = runID, 
				userID = userID,
				problemID = problemID,
				status = "queueing",
				memory = memory,
				runTime = runTime,
				codeLength = codeLength,
				date = date,
				timestamp = timestamp,
				code = code)
			Judge(submit)
		return HttpResponse(str(date))
	else:
		return render(request, 'cugbacm/submit.html', {'form': form})
		
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
		User(
			userID = userID, 
			password = password,
			session = session,
			specialty = specialty,
			tel = tel,
			email = email,
			nickname = nickname).save()
		return HttpResponse("register success!")
	else:
		return render(request, 'cugbacm/register.html', {})

def login(request):
	if request.method == 'POST':
		userID = request.POST['userID']
		password = request.POST['password']
		try:
			user = User.objects.get(userID = userID)
			if user.password != password:
				return HttpResponse("password error!")
			else:
				return HttpResponse("login success!")
		except Exception as err:
			return HttpResponse(userID+" does not exsits")
	else:
		return render(request, 'cugbacm/login.html', {})

def addProblem(request):
	form = ProblemForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			problemID = form.cleaned_data['problemID']
			title = form.cleaned_data['title']
			timeLimit = form.cleaned_data['timeLimit']
			memoryLimit = form.cleaned_data['memoryLimit']
			acceptedSubmission = form.cleaned_data['acceptedSubmission']
			totalSubmission = form.cleaned_data['totalSubmission']
			description = form.cleaned_data['description']
			input = form.cleaned_data['input']
			output = form.cleaned_data['output']
			sampleInput = form.cleaned_data['sampleInput']
			sampleOutput = form.cleaned_data['sampleOutput']
			author = form.cleaned_data['author']
			Problem(
				problemID = problemID,
				title = title,
				timeLimit = timeLimit,
				memoryLimit = memoryLimit,
				acceptedSubmission = acceptedSubmission,
				totalSubmission = totalSubmission,
				description = description,
				input = input,
				output = output,
				sampleInput = sampleInput,
				sampleOutput = sampleOutput,
				author = author).save()
			return HttpResponse("addProblem success!")
	else:
		return render(request, 'cugbacm/addProblem.html', {'form': form})
