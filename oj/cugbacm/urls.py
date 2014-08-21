from django.conf.urls import patterns, url
from cugbacm import views

urlpatterns = patterns('',
  url(r'^register/$', views.register, name = 'register'),
  url(r'^problem/(?P<problem_id>\d+)/submit$', views.submit, name = 'submit'),
  url(r'^contest/(?P<contest_id>\d+)$', views.contest, name = 'contest'),
  url(r'^contest/(?P<contest_id>\d+)/submitList$', views.contestSubmitList, name = 'contestSubmitList'),
  url(r'^contest/(?P<contest_id>\d+)/rankList$', views.contestRankList, name = 'contestRankList'),
  url(r'^addProblem/$', views.addProblem, name = 'addProblem'),
  url(r'^login/$', views.login, name = 'login'),
  url(r'^problemList/$', views.problemList, name = 'problemList'),
  url(r'^contestList/$', views.contestList, name = 'contestList'),
  url(r'^testdata/$', views.testdata, name = 'testdata'),
  url(r'^submitList/$', views.submitList, name = 'submitList'),
  url(r'^userList/$', views.userList, name = 'userList'),
  url(r'^gettest/$', views.gettest, name = 'gettest'),
  url(r'^problem/(?P<problem_id>\d+)$', views.problem, name = 'problem'),
  url(r'^showCode/(?P<submit_id>\d+)$', views.showCode, name = 'showCode'),
  url(r'^userInfo/(?P<user_id>\w+)$', views.userInfo, name = 'userInfo'),
  url(r'^contest/(?P<contest_id>\d+)/problem/(?P<problem_id>\d+)$',views.contestProblem, name = 'contestProblem'),
  )
