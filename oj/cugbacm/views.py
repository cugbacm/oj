#!/usr/bin/env python
import sys
from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit, Problem, Contest
from django.http import HttpResponse, HttpResponseRedirect
from cugbacm.forms import UserRegisterForm, SubmitForm, ProblemForm, LoginForm
#from celery.decorators import task
from celery.task import task
from celery import current_task
from django.views.decorators.csrf import csrf_exempt
import json
from core_hq import main
from core_hq import UserSubmit
import os
import re
# Create your views here.

def ProcessMail(inputMail):  
	if len(inputMail) > 7:
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", inputMail) != None:
			return True
		else:
			return False
	return False 

@task
def Judge(submit):
	problem = Problem.objects.get(problemID = submit.problemID)
	user = User.objects.get(userID = submit.userID)
	user_submit = UserSubmit(
		solution_id = submit.id,
		problem_id = submit.problemID,
		language = submit.language,
		user_id = submit.userID,
		program = submit.code,
		mem_limit = problem.memoryLimit,
		time_limit = problem.timeLimit
	)
	result = main(user_submit)
	submit.status = result['result']
	submit.codeLength = result['codeLength']
	submit.runTime = result['take_time']
	submit.memory = result['take_memory']
	submit.save()
	print submit.status

	if submit.status == "Accepted":
		if Submit.objects.filter(userID = user.userID, problemID = submit.problemID).count() == 1:
			user.accepted = user.accepted + 1
		problem.ac = problem.ac + 1
	elif submit.status == "Time Limit Exceeded":
		problem.tle = problem.tle + 1
	elif submit.status == "Memory Limit Exceeded":
		problem.mle = problem.mle + 1
	elif submit.status == "Wrong Answer":
		problem.wa = problem.wa + 1
	elif submit.status == "Runtime Error":
		problem.re = problem.re + 1
	elif submit.status == "Compile Error":
		problem.ce = problem.ce + 1
	elif submit.status == "Presentation Error":
		problem.pe = problem.pe + 1
	elif submit.status == "System Error":
		problem.se = problem.se + 1

	problem.totalSubmission = problem.totalSubmission + 1
	user.total = user.total + 1
	user.save()
	problem.save()
	return submit.status

def submit(request, problem_id):
	try:
		user = User.objects.get(userID = request.session['userID'])
	except:
		return HttpResponseRedirect("/index/login")
	if request.method == 'POST':
		code = request.POST['code']
		language = request.POST['language']
		for i in range(1000):
			submit = Submit(
				runID = 111, 
				userID = request.session["userID"],
				problemID = problem_id,
				status = "queueing",
				memory = 10000,
				runTime = 1000,
				codeLength = 100,
				language = language,
				code = code)
			submit.save()
			Judge(submit)
		return HttpResponseRedirect("/index/submitList")
	else:
		return render(request, 'cugbacm/submit.html', {'problem_id':problem_id})

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
					submits = submits.filter(userID = userIDSearch)
				if problemIDSearch.strip():
					submits = submits.filter(problemID = problemIDSearch)
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

def userList(request):
	try:
		user = User.objects.get(userID = request.session['userID'])
	except:
		return HttpResponseRedirect("/index/login")
	users = User.objects.all().order_by('-accepted')
	return render(request, 'cugbacm/userList.html', {'users': users, 'userID':request.session['userID']})


def userInfo(request):
	try:
		user = User.objects.get(userID = request.session['userID'])
	except:
		return HttpResponseRedirect("/index/login")

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
			return HttpResponse("password error")
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
				return HttpResponse("password and confirmPassword is not the same!")
	else:
		return render(request, 'cugbacm/userInfo.html', {'userID':request.session['userID'],'user': user})

		
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
		if len(password) < 10:
			return HttpResponse("The length of password should not less than 10.")
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
	except:
		return HttpResponseRedirect("/index/login")
	if request.method == 'POST':
		#problemID = request.POST['problemID']
		problemID = Problem.objects.count()+1000
		title = request.POST['title']
		timeLimit = request.POST['timeLimit']
		memoryLimit = request.POST['memoryLimit']
		description = request.POST['description']
		input = request.POST['input']
		output = request.POST['output']
		sampleInput = request.POST['sampleInput']
		sampleOutput = request.POST['sampleOutput']
		author = request.POST['source']
		Problem(
			problemID = problemID,
			title = title,
			timeLimit = timeLimit,
			memoryLimit = memoryLimit,
			description = description,
			input = input,
			output = output,
			sampleInput = sampleInput,
			sampleOutput = sampleOutput,
			author = author).save()
		return HttpResponseRedirect("/index/problemList")
	else:
		return render(request, 'cugbacm/addProblem.html', {})

def handle_uploaded_file(dataIn, dataOut, problemID):
	os.makedirs('/home/cugbacm/Documents/data_dir/%s'% problemID)
	with open('/home/cugbacm/Documents/data_dir/%s/data.in' % problemID, 'wb+') as info:
		for chunk in dataIn.chunks():
			info.write(chunk)
	with open('/home/cugbacm/Documents/data_dir/%s/data.out' % problemID, 'wb+') as info:
		for chunk in dataOut.chunks():
			info.write(chunk)

def problem(request, problem_id):
	try:
		user = User.objects.get(userID = request.session['userID'])
	except:
		return HttpResponseRedirect("/index/login")
	problem = Problem.objects.get(problemID=problem_id)
	user = User.objects.get(userID = request.session['userID'])
	submits = Submit.objects.filter(problemID = problem_id, userID = user.userID).order_by('-id')
	if request.method == 'POST':
		code = request.POST['code']
		language = request.POST['language']
		for i in range(1):
			submit = Submit(
				runID = 111, 
				userID = request.session["userID"],
				problemID = problem_id,
				status = "queueing",
				memory = 10000,
				runTime = 1000,
				codeLength = 100,
				language = language,
				code = code)
			submit.save()
			Judge.delay(submit)
		
		return HttpResponseRedirect("/index/problem/" + str(problem_id))
	else:
		try:
			submit = Submit.objects.get(id = request.GET.get('submit'))
			if submit.userID == user.userID and str(submit.problemID) == str(problem_id):
				return render(request, 'cugbacm/problem.html', {'problem': problem, 'userID' :user.userID, 'submit':submit, 'submits':submits})
			else:
				return HttpResponseRedirect("/index/problem/" + str(problem_id))
		except:
			return render(request, 'cugbacm/problem.html', {'problem': problem, 'userID' :user.userID, 'submits':submits})
	
def problemList(request):
	try:
		user = User.objects.get(userID = request.session['userID'])
		problems = Problem.objects.all()
		if request.method == 'POST':
			problemID = request.POST['problemID']
			problemTitle = request.POST['problemTitle']
			problemAuthor = request.POST['problemAuthor']
			try:
				if problemID.strip():
					problems = problems.filter(problemID = problemID)
				if problemTitle.strip():
					problems = problems.filter(title = problemTitle)
				if problemAuthor.strip():
					problems = problems.filter(author = problemAuthor)
				return render(
					request, 
					'cugbacm/problemList.html', 
					{
						'problems': problems, 
						'userID': request.session["userID"],
						'problemID': problemID,
						'problemTitle': problemTitle,
						'problemAuthor': problemAuthor
					}
				)
			except:
				return render(request, 'cugbacm/problemList.html', {'problems': {}, 'userID':request.session["userID"]})
		else:
			return render(request, 'cugbacm/problemList.html', {'problems': problems, 'userID':request.session["userID"]})
	except:
		return HttpResponseRedirect("/index/login")

def showCode(request, submit_id):
	try:
		user = User.objects.get(userID = request.session['userID'])
	except:
		return HttpResponseRedirect("/index/login")
	
	return render(request, 'cugbacm/showCode.html', {'submit_code': Submit.objects.get(id = submit_id).code}) 

def contestList(request):
	try:
		user = User.objects.get(userID = request.session['userID'])
	except:
		return HttpResponseRedirect("/index/login")
	contests = Contest.objects.all()
	return render(request, 'cugbacm/contestList.html', {'contests': contests, 'user': user})

def hello(request):
	return render(request, 'cugbacm/hello.html', {})
