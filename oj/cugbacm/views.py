from django.shortcuts import render
from django.template import Context, loader
from cugbacm.models import User, Submit
from django.http import HttpResponse
import pika
import CompileCpp
from cugbacm.forms import UserRegister, Submit
# Create your views here.

def submit(request):
	form = Submit(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			runID = form.cleaned_data['runID']
			userID = form.cleaned_data['userID']
			problemID = form.cleaned_data['problemID']
			result = form.cleaned_data['result']
			memory = form.cleaned_data['memory']
			time = form.cleaned_data['time']
			codeLength = form.cleaned_data['codeLength']
			date = form.cleaned_data['date']
			timestamp = form.cleaned_data['timestamp']
			code = form.cleaned_data['code']
			'''Submit(
				runID = runID, 
				userID = userID,
				problemID = problemID,
				result = result,
				memory = memory,
				time = time,
				codeLength = codeLength,
				date = date,
				timestamp = timestamp,
				code = code).save()'''

			result = CompileCpp.main('1000', 'c++', code)
			return HttpResponse(result)
	else:
		return render(request, 'cugbacm/submit.html', {'form': form})
		
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
			#connection = pika.BlockingConnection(pika.ConnectionParameters(
       		#host='localhost'))
			#channel = connection.channel()

			#channel.queue_declare(queue='task_queue', durable=True)

			message = name
			#channel.basic_publish(
			#	exchange='',
    		#	routing_key='task_queue',
    		#	body=message,
    		#	properties=pika.BasicProperties(
    		#	delivery_mode = 2, # make message persistent
			#))
			#print " [x] Sent %r" % (message,)
			#connection.close()
			result = CompileCpp.main('1000', 'c++', message)
			return HttpResponse(result)
	else:
		return render(request, 'cugbacm/register.html', {'form': form})
