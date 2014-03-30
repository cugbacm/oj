from django import forms
from cugbacm.models import User, Submit, Problem

class UserRegisterForm(forms.Form):
	userID = forms.CharField(label = 'userID')
	password = forms.CharField(widget = forms.PasswordInput, label = 'password')
	confirmPassword = forms.CharField(widget = forms.PasswordInput, label = 'confirmPassword')
	session = forms.CharField(label = 'session')
	specialty = forms.CharField(label = 'specialty')
	tel = forms.CharField(label = 'tel')
	email = forms.EmailField(label = 'email')
	nickname = forms.CharField(label = 'nickname')

class SubmitForm(forms.Form):
	runID = forms.IntegerField(label = 'runID')
	userID = forms.CharField(label = 'userID')
	problemID = forms.CharField(label = 'problemID')
	language = forms.ChoiceField(label = 'language', choices = [('g++','g++'),('gcc','gcc'),('java','java'),('python2','python2'),('python3','python3')])
	status = forms.CharField(label = 'status')
	memory = forms.IntegerField(label = 'memory')
	runTime = forms.IntegerField(label = 'runTime')
	codeLength = forms.IntegerField(label = 'codeLength')
	date = forms.DateField(label = 'date')
	timestamp = forms.TimeField(label = 'timestamp')
	code = forms.CharField(label = 'code', widget=forms.Textarea)

class ProblemForm(forms.Form):
	problemID = forms.IntegerField(label = 'problemID')
	title = forms.CharField(label = 'title')
	timeLimit = forms.IntegerField(label = 'timeLimit')
	memoryLimit = forms.IntegerField(label = 'memoryLimit');
	acceptedSubmission = forms.IntegerField(label = 'acceptedSubmission');
	totalSubmission = forms.IntegerField(label = 'totalSubmission');
	description = forms.CharField(label = 'description', widget = forms.Textarea);
	input = forms.CharField(label = 'input', widget = forms.Textarea);
	output = forms.CharField(label = 'output', widget = forms.Textarea);
	sampleInput = forms.CharField(label = 'sampleInput', widget = forms.Textarea);
	sampleOutput = forms.CharField(label = 'sampleOutput', widget = forms.Textarea);
	author = forms.CharField(label = 'author')

class LoginForm(forms.Form):
	userID = forms.CharField(label = 'userID')
	password = forms.CharField(widget = forms.PasswordInput, label = 'password')
			