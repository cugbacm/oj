"""oj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from cugbacm.views import ProblemView
from cugbacm.views import LoginView
from cugbacm.views import ProblemListView
from cugbacm.views import SubmitListView
from cugbacm.views import UserListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^problem/(?P<problem_id>\d+)$', login_required(ProblemView.as_view()), name='problem'),
    url(r'^accounts/login/', LoginView.as_view(), name='login'),
    url(r'^problem_list/', login_required(ProblemListView.as_view()), name='problem_list'),
    url(r'^submit_list/', login_required(SubmitListView.as_view()), name='submit_list'),
    url(r'^user_list/', login_required(UserListView.as_view()), name='user_list'),
]
