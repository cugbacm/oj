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
