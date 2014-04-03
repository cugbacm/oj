#!/usr/bin/env python
import pika
import sys
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem
from django.http import HttpResponse, HttpResponseRedirect
from cugbacm.forms import UserRegisterForm, SubmitForm, ProblemForm, LoginForm
from celery.decorators import task
from CompileCpp import main
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@task
def Judge(submit):
	submit.status = main(submit.problemID, 'c++', submit.code)
	submit.save()
	return submit.status

def submit(request, problem_id):
	try:
		user = User.objects.get(userID = request.session['userID'])
		if request.method == 'POST':
			#runID = form.cleaned_data['runID']
			#userID = form.cleaned_data['userID']
			problemID = request.POST['problemID']
			#status = form.cleaned_data['status']
			#memory = form.cleaned_data['memory']
			#runTime = form.cleaned_data['runTime']
			#codeLength = form.cleaned_data['codeLength']
			#date = form.cleaned_data['date']
			#timestamp = form.cleaned_data['timestamp']
			code = request.POST['code']
			language = request.POST['language']
			submit = Submit(
				runID = 111, 
				userID = request.session["userID"],
				problemID = request.POST['problemID'],
				status = "queueing",
				memory = 10000,
				runTime = 1000,
				codeLength = 100,
				language = language,
				code = code)
			print submit.date
			Judge(submit)
			return HttpResponseRedirect("/index/submitList")
		else:
			return render(request, 'cugbacm/submit.html', {'problem_id':problem_id})
	except:
		return HttpResponseRedirect("/index/login")

def submitList(request):
	try:
		user = User.objects.get(userID = request.session['userID'])
		submits = Submit.objects.all().order_by('-id')
		return render(request, 'cugbacm/submitList.html', {'submits': submits, 'userID':request.session['userID'] })
	except:
		return HttpResponseRedirect("/index/login")

def userInfo(request):
	try:
		user = User.objects.get(userID = request.session['userID'])
		if request.method == 'POST':
			userID = request.POST['userID']
			oldPassword = request.POST['oldPassword']
			password = request.POST['password']
			confirmPassword = request.POST['confirmPassword']
			session = request.POST['session']
			specialty = request.POST['specialty']
			tel = request.POST['tel']
			email = request.POST['email']
			nickname = request.POST['nickname']
			if oldPassword != user.password:
				HttpResponse("error")
			else:
				if password.strip() != '' and password == confirmPassword:
					user.password = password
				user.session = session
				user.specialty = specialty
				user.tel = tel
				user.email = email
				user.nickname = nickname
				user.save()
				return render(request, 'cugbacm/userInfo.html', {'userID':request.session['userID'],'user': user})
		else:
			return render(request, 'cugbacm/userInfo.html', {'userID':request.session['userID'],'user': user})
	except:
		return HttpResponseRedirect("/index/login")
		
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
		request.session['userID'] = userID
		return HttpResponseRedirect("/index/problemList")
	else:
		return render(request, 'cugbacm/register.html', {})
@csrf_exempt
def login(request):
	if request.method == 'POST':

		'''userID = request.POST['userID']
		password = request.POST['password']'''
		userID = request.POST['userID']
		password = request.POST['password']
		print userID
		print password
		try:
			user = User.objects.get(userID = userID)
			if user.password != password:
				return HttpResponse("password error!")
			else:
				request.session["userID"] = userID
				return HttpResponse("success")
		except:
			return HttpResponse(userID+" does not exsits")
	else:
		try: 
			del request.session['userID'] 
		except:
			pass
		return render(request, 'cugbacm/login.html', {})

@csrf_exempt
def gettest(request):
	a = {"aaData":[["1","2","3","4","5"],["6","7","8","9","10"]]}
	return HttpResponse(json.dumps(a))
def testdata(request):
	return render(request, 'cugbacm/testdata.html', {})
def addProblem(request):
	try:
		user = User.objects.get(userID = request.session['userID'])
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
	except:
		return HttpResponseRedirect("/index/login")
def problem(request, problem_id):
	try:
		user = User.objects.get(userID = request.session['userID'])
		problem = Problem.objects.get(problemID=problem_id)
		return render(request, 'cugbacm/problem.html', {'problem': problem})
	except:
		HttpResponseRedirect("/index/login")
def problemList(request):
	try:
		user = User.objects.get(userID = request.session['userID'])
		problems = Problem.objects.all()
		return render(request, 'cugbacm/problemList.html', {'problems': problems, 'userID':request.session["userID"]})
	except:
		return HttpResponseRedirect("/index/login")
