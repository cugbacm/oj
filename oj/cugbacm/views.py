from django.shortcuts import render
from cugbacm import views
# Create your views here.

urlpatterns = patterns('',
	url(r'^index/$', views.index, name = 'index'),
)
