from django.conf.urls import patterns, url
import views.register
import views.contest
import views.contest_submit_list
import views.contest_rank_list
import views.login
import views.problem_list
import views.contest_list
import views.submit_list
import views.user_list
import views.problem
import views.user_info
import views.contest_problem
import views.rejudge
import views.permit_judge
import views.test
import views.contest_massuser
import views.uploadfile

urlpatterns = patterns('',
  url(r'^register/$', views.register.register, name = 'register'),
  url(r'^massproduction/$', views.contest_massuser.production, name = 'massuser_production'),
  url(r'^uploadfile/$', views.uploadfile.uploadfile, name = 'uploadfile'),
  url(r'^massdelete/$', views.contest_massuser.delete, name = 'massuser_delete'),
  url(r'^contest/(?P<contest_id>\d+)$', views.contest.contest, name = 'contest'),
  url(r'^contest/(?P<contest_id>\d+)/submitList$', views.contest_submit_list.contestSubmitList, name = 'contestSubmitList'),
  url(r'^contest/(?P<contest_id>\d+)/rankList$', views.contest_rank_list.contestRankList, name = 'contestRankList'),
  url(r'^login/$', views.login.login, name = 'login'),
  url(r'^problemList/$', views.problem_list.problemList, name = 'problemList'),
  url(r'^contestList/$', views.contest_list.contestList, name = 'contestList'),
  url(r'^submitList/$', views.submit_list.submitList, name = 'submitList'),
  url(r'^userList/$', views.user_list.userList, name = 'userList'),
  url(r'^problem/(?P<problem_id>\d+)$', views.problem.problem, name = 'problem'),
  url(r'^userInfo/(?P<user_id>\w+)$', views.user_info.userInfo, name = 'userInfo'),
  url(r'^test/$', views.test.test, name = 'test'),
  url(r'^contest/(?P<contest_id>\d+)/problem/(?P<problem_id>\d+)$', views.contest_problem.contestProblem, name = 'contestProblem'),
  url(r'^rejudge/(?P<run_id>\d+)$', views.rejudge.rejudge, name = 'rejudge'),
  url(r'^rejudge/(?P<start_run_id>\d+)to(?P<end_run_id>\d+)$', views.rejudge.rejudgeRange, name = 'rejudge'),
  url(r'^permit_judge/(?P<contest_id>\d+)$', views.permit_judge.permit_judge, name = 'permit_judge')
)
