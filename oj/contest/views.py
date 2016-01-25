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
from oj.task import judge

# Create your views here.
# 题目列表
class ContestListView(BaseListView):
    template_name = 'contest/contest_list.html'
    def get(self, request):
        args = {}
        contest_list = Contest.objects.all()
        args.update(self.paginate(request, contest_list, '/contest_list', 'contests', num_per_page=5))
        return render_to_response(ContestListView.template_name, args)

class ContestInfoView(View):
    template_name = 'contest/contest_info.html'
    def get(self, request, contest_id):
        try:
            contest = Contest.objects.get(contest_id=contest_id)
            return render_to_response(ContestInfoView.template_name, {'contest': contest})
        except:
            return HttpResponse("contest does not exist " + str(contest_id))
