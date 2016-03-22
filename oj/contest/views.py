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

from .models import Contest
from .models import ContestUser
from .models import ContestProblem
from .models import ContestSubmit
from cugbacm.views import BaseListView
from cugbacm.models import User
from oj.task import judge

# Create your views here.
# 比赛列表
class ContestListView(BaseListView):
    template_name = 'contest/contest_list.html'
    def get(self, request):
        args = {}
        contest_list = Contest.objects.all()
        args.update(self.paginate(request, contest_list, '/contest_list', 'contests', num_per_page=5))
        return render_to_response(ContestListView.template_name, args)

# 比赛信息
class ContestInfoView(View):
    template_name = 'contest/contest_info.html'
    def get(self, request, contest_id):
        try:
            contest = Contest.objects.get(contest_id=contest_id)
            return render_to_response(ContestInfoView.template_name, {'contest': contest})
        except:
            return HttpResponse("contest does not exist " + str(contest_id))

# 比赛题目列表
class ContestProblemListView(BaseListView):
    template_name = 'contest/contest_problem_list.html'
    def get(self, request, contest_id):
        args = {}
        try:
            contest = Contest.objects.get(contest_id=contest_id)
            args["contest"] = contest
        except:
            return HttpResponse("contest does not exist" + str(contest_id))
        problem_list = ContestProblem.objects.filter(contest=contest)
        args.update(self.paginate(request, problem_list, '/contest/' + str(contest_id) + '/problem_list', 'contest_problems', num_per_page=5))
        return render_to_response(ContestProblemListView.template_name, args)

# 比赛题目详情
class ContestProblemView(View):
    template_name = 'contest/contest_problem.html'

    def get(self, request, contest_id, id_in_contest):
        args = {}
        try:
            contest = Contest.objects.get(contest_id=contest_id)
            args["contest"] = contest
            print id_in_contest
            problem = ContestProblem.objects.get(contest=contest, id_in_contest=id_in_contest)
            args["problem"] = problem
            return render_to_response(ContestProblemView.template_name, args)
        except:
            return HttpResponse("problem does not exist " + str(contest_id) + "_" + str(id_in_contest))

    def post(self, request, contest_id, id_in_contest):
        user = User.objects.get(user=request.user)
        contest_user = ContestUser.objects.get(raw_user=user)
        contest = Contest.objects.get(contest_id=contest_id)
        problem = ContestProblem.objects.get(contest=contest, id_in_contest=id_in_contest)
        code = request.POST['code']
        language = request.POST['language']
        submit = ContestSubmit(user=contest_user,
                               contest=contest,
                               problem=problem,
                               language=language,
                               status="Queueing",
                               code=code)
        judge.delay(submit)
        return HttpResponse(submit)

# 比赛提交列表
class ContestSubmitListView(BaseListView):
    template_name = 'contest/contest_submit_list.html'
    def get(self, request, contest_id):
        contest = Contest.objects.get(contest_id=contest_id)
        args = {}
        args["contest"] = contest
        submit_list = ContestSubmit.objects.all().order_by('-contest_submit_id')
        args.update(self.paginate(request, submit_list, '/contest/' + str(contest_id) + '/submit_list', 'submits', num_per_page=5))
        return render_to_response(ContestSubmitListView.template_name, args)

# 排名
class ContestRankView(BaseListView):
    template_name = 'contest/contest_rank.html'
    def get(self, request, contest_id):
        contest = Contest.objects.get(contest_id=contest_id)
        args = {}
        args["contest"] = contest
        user_list = ContestUser.objects.all().order_by('-ac', 'penalty_time')
        args.update(self.paginate(request, user_list, '/contest/' + str(contest_id) + '/rank', 'users', num_per_page=5))
        return render_to_response(ContestRankView.template_name, args)
