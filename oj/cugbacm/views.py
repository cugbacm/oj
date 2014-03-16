from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit
from django.http import HttpResponse
from cugbacm.forms import UserRegister
# Create your views here.

def register(request):
	form = UserRegister(request.POST)
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
			return HttpResponse("OK!")
	else:
		return render(request, 'cugbacm/register.html', {'form': form})
