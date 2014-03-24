#!/usr/bin/env python
import pika
import sys
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem
from django.http import HttpResponse
from cugbacm.forms import UserRegisterForm, SubmitForm, ProblemForm
# Create your views here.

def sendMessage(msg):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='task_queue', durable=True)
	channel.basic_publish(
		exchange='',
	    routing_key='task_queue',
	    body=msg,
	    properties=pika.BasicProperties(
	    delivery_mode = 2, # make message persistent
	))
	connection.close()

def submit(request):
	form = SubmitForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			runID = form.cleaned_data['runID']
			userName = form.cleaned_data['userName']
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
				userName = userName,
				problemID = problemID,
				status = "queueing",
				memory = memory,
				runTime = runTime,
				codeLength = codeLength,
				date = date,
				timestamp = timestamp,
				code = code)
			sendMessage(submit)
		return HttpResponse(str(date))
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
