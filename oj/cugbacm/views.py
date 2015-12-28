# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View, DetailView
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Problem
from .models import Submit

# Create your views here.
# 题目详情
class ProblemView(View):
    template_name = 'cugbacm/problem.html'

    def get(self, request, problem_id):
        try:
            problem = Problem.objects.get(problem_id=problem_id)
            return render_to_response(ProblemView.template_name, {'problem': problem})
        except:
            return HttpResponse("problem does not exist " + str(problem_id))

    def post(self, request, problem_id):
        return HttpResponse('problem view post' + str(problem_id))

# 登陆界面
class LoginView(View):
    template_name = 'cugbacm/login.html'

    def go_to_next(self, request):
        # 默认跳转到problem_list页面
        next = '/problem_list'
        if request.GET.get('next'):
            # 如果有指定的跳转页，则跳转到该页面
            next = request.GET.get('next')
        return HttpResponseRedirect(next)

    def get(self, request):
        return render_to_response(LoginView.template_name, {'full_path': request.get_full_path()})
        # 如果用户已经登录就跳转
        if request.user.is_authenticated():
            return self.go_to_next(request)
        else:
            return render_to_response(LoginView.template_name, {'full_path': request.get_full_path()})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.go_to_next(request)
        return HttpResponseRedirect('/accounts/login')

# 题目列表
class ProblemListView(View):
    template_name = 'cugbacm/problem_list.html'
    def get(self, request):
        return render_to_response(ProblemListView.template_name)

# 提交列表
class SubmitListView(View):
    template_name = 'cugbacm/submit_list.html'
    def get(self, request):
        return render_to_response(SubmitListView.template_name)
