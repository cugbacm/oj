from django import forms

class UserRegister(forms.Form):
	name = forms.CharField(label = 'name')
	password = forms.CharField(widget = forms.PasswordInput, label = 'password')
	confirmPassword = forms.CharField(widget = forms.PasswordInput, label = 'confirmPassword')
	session = forms.CharField(label = 'session')
	specialty = forms.CharField(label = 'specialty')
	tel = forms.CharField(label = 'tel')
	email = forms.EmailField(label = 'email')
	nickname = forms.CharField(label = 'nickname')

class Submit(forms.Form):
	runID = forms.IntegerField(label = 'runID', required = False)
	userID = forms.CharField(label = 'userID', required = False)
	problemID = forms.IntegerField(label = 'problemID', required = False)
	result = forms.CharField(label = 'result', required = False)
	memory = forms.CharField(label = 'memory', required = False)
	time = forms.CharField(label = 'time', required = False)
	codeLength = forms.CharField(label = 'codeLength', required = False)
	date = forms.DateField(label = 'date', required = False)
	timestamp = forms.TimeField(label = 'timestamp', required = False)
	code = forms.CharField(label = 'code', widget=forms.Textarea)
		
