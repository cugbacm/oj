from django.conf.urls import patterns, url
from cugbacm import views

urlpatterns = patterns('',
	url(r'^register/$', views.register, name = 'register'),
	url(r'^submit/$', views.submit, name = 'submit'),
)
