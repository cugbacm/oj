# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.generic import View, DetailView
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import User

# Create your views here.
# 题目详情
class ProblemView(View):
    def get(self, request, problem_id):
        return HttpResponse('problem view get ' + str(problem_id))

    def post(self, request, problem_id):
        return HttpResponse('problem view post' + str(problem_id))

# 登陆界面
class LoginView(View):
    template_name = 'cugbacm/login.html'
    def get(self, request):
        return render_to_response(LoginView.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("login!")
            else:
                return HttpResponse("fuck")
        else:
            return HttpResponse("fuck")

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
