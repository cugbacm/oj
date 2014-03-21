from django import forms

class UserRegisterForm(forms.Form):
	name = forms.CharField(label = 'name')
	password = forms.CharField(widget = forms.PasswordInput, label = 'password')
	confirmPassword = forms.CharField(widget = forms.PasswordInput, label = 'confirmPassword')
	session = forms.CharField(label = 'session')
	specialty = forms.CharField(label = 'specialty')
	tel = forms.CharField(label = 'tel')
	email = forms.EmailField(label = 'email')
	nickname = forms.CharField(label = 'nickname')

class SubmitForm(forms.Form):
	runID = forms.CharField(label = 'runID')
	userID = forms.CharField(label = 'userID')
	problemID = forms.CharField(label = 'problemID')
	status = forms.CharField(label = 'status')
	memory = forms.CharField(label = 'memory')
	time = forms.CharField(label = 'time')
	codeLength = forms.CharField(label = 'codeLength')
	date = forms.DateField(label = 'date')
	timestamp = forms.TimeField(label = 'timestamp')
	code = forms.CharField(label = 'code', widget=forms.Textarea)
		
