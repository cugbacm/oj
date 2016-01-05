# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View, DetailView
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Problem
from .models import Submit
from oj.task import judge

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
        user = User.objects.get(user=request.user)
        problem = Problem.objects.get(problem_id=problem_id)
        code = request.POST['code']
        language = request.POST['language']
        submit = Submit(user=user,
                        problem=problem,
                        language=language,
                        status="Queueing",
                        code=code)
        judge.delay(submit)
        return HttpResponse(submit)

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

class BaseListView(View):
    def paginate(self, request, object_list, url, objects_name='objects', num_per_page=50):
        paginator = Paginator(object_list, num_per_page)
        page = request.GET.get('page')
        try:
            objects = paginator.page(page)
            page = int(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            objects = paginator.page(1)
            page = 1
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            objects = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        pages_url = []
        for i in range(1, paginator.num_pages + 1):
            pages_url.append(url + '?page='+ str(i))
        pre_page = max(1, page - 1)
        pre_url = url + '?page=' + str(pre_page)
        next_page = min(paginator.num_pages, page + 1)
        next_url = url + '?page=' + str(next_page)
        return {
            objects_name: objects,
            'pages_url': pages_url,
            'pre_url': pre_url,
            'next_url': next_url,
            'now_page': page
        }

# 题目列表
class ProblemListView(BaseListView):
    template_name = 'cugbacm/problem_list.html'
    def get(self, request):
        args = {}
        problem_list = Problem.objects.all()
        args.update(self.paginate(request, problem_list, '/problem_list', 'problems', num_per_page=5))
        return render_to_response(ProblemListView.template_name, args)

# 提交列表
class SubmitListView(BaseListView):
    template_name = 'cugbacm/submit_list.html'
    def get(self, request):
        args = {}
        submit_list = Submit.objects.all().order_by('-submit_id')
        args.update(self.paginate(request, submit_list, '/submit_list', 'submits', num_per_page=5))
        return render_to_response(SubmitListView.template_name, args)

# 用户列表
class UserListView(BaseListView):
    template_name = 'cugbacm/user_list.html'
    def get(self, request):
        args = {}
        user_list = User.objects.all().order_by('ac')
        args.update(self.paginate(request, user_list, '/user_list', 'users', num_per_page=5))
        return render_to_response(UserListView.template_name, args)
