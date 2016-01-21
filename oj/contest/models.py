# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from cugbacm.models import User, Problem
from cugbacm.judge import judge_submit
# Create your models here.

class Contest(models.Model):
    '''
    比赛的一些基础字段
    '''
    # 比赛id
    contest_id = models.AutoField(primary_key=True)
    # 作者
    author = models.ForeignKey(User, related_name='author_contest')
    # 标题
    title = models.CharField(max_length = 100)
    # 开始时间
    start_time = models.DateTimeField()
    # 结束时间
    endTime = models.DateTimeField()
    # 当前状态
    status_option = (
        ("pending", "pending"),
        ("running", "running"),
        ("end", "end"),
    )
    status = models.CharField(choices=status_option, max_length=50)
    # 是否是公开的
    public = models.BooleanField(default=True)
    # 加密方式
    encryption_mode_option = (
        # 密码验证
        ("password", "password"),
        # 手动添加哪些用户可以进行比赛
        ("manual", "manual"),
    )
    encryption_mode = models.CharField(choices=encryption_mode_option, max_length=20)

    def __unicode__(self):
        return self.title + "\t" + self.author

class ContestUser(models.Model):
    '''
    当一个比赛的加密方式是manual时，需要存比赛允许哪些用户参加
    '''
    raw_user = models.ForeignKey(User, related_name='user_contest')
    contest = models.ForeignKey(Contest, related_name='contest_user')
    # AC的数量
    ac = models.IntegerField(default=0);
    # WA的数量
    wa = models.IntegerField(default=0);
    # TLE的数量
    tle = models.IntegerField(default=0);
    # MLE的数量
    mle = models.IntegerField(default=0);
    # PE的数量
    pe = models.IntegerField(default=0);
    # CE的数量
    ce = models.IntegerField(default=0);
    # SE的数量
    se = models.IntegerField(default=0);
    # RE的数量
    re = models.IntegerField(default=0);

class ContestProblem(models.Model):
    '''
    比赛中题库中的题目
    '''
    contest = models.ForeignKey(Contest, related_name='contest_problem')
    # 在题库中原始的那一题
    raw_problem = models.ForeignKey(Problem, related_name='problem_contest')
    # 显示在比赛中的id 比如ABCD
    id_in_contest = models.CharField(max_length=10)
    # AC的数量
    ac = models.IntegerField(default=0);
    # WA的数量
    wa = models.IntegerField(default=0);
    # TLE的数量
    tle = models.IntegerField(default=0);
    # MLE的数量
    mle = models.IntegerField(default=0);
    # PE的数量
    pe = models.IntegerField(default=0);
    # CE的数量
    ce = models.IntegerField(default=0);
    # SE的数量
    se = models.IntegerField(default=0);
    # RE的数量
    re = models.IntegerField(default=0);

class ContestSubmit(models.Model):
    '''
    比赛中的提交
    '''
    # 属于哪个比赛
    contest = models.ForeignKey(Contest, related_name='contest_submit')
    # 提交id
    contest_submit_id = models.AutoField(primary_key=True)
    # 用户
    user = models.ForeignKey(ContestUser, related_name='contest_user_submit')
    # 题目
    problem = models.ForeignKey(ContestProblem, related_name='contest_problem_submit')
    # 状态
    status_option = (
        ("Queueing", "Queueing"),
        ("System Error", "System Error"),
        ("Runtime Error", "Runtime Error"),
        ("Compile Error", "Compile Error"),
        ("Time Limit Exceeded", "Time Limit Exceeded"),
        ("Memory Limit Exceeded", "Memory Limit Exceeded"),
        ("Wrong Answer", "Wrong Answer"),
        ("Accepted", "Accepted"),
        ("Judging", "Judging"),
        ("Presentation Error", "Presentation Error"),
    )
    status = models.CharField(choices=status_option, max_length=100)
    # 所占内存kb为单位
    memory = models.IntegerField(default=0, blank=True)
    # 运行时间ms为单位
    run_time = models.IntegerField(default=0, blank=True)
    # 语言
    language_option = (
        ("g++", "g++"),
        ("gcc", "gcc"),
        ("java", "java"),
        ("python2", "python2"),
        ("python3", "python3"),
    )
    language = models.CharField(choices=language_option, max_length=100)
    # 代码长度b为单位
    code_length = models.IntegerField(default=0, blank=True)
    # 提交时间
    date = models.DateTimeField(auto_now_add = True, auto_now=False)
    # 源码
    code = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.submit_id) + "\t" + str(self.user) + "\t" + str(self.problem.title)

    def judge(self):
        # 判题内核
        result = judge_submit(self.contest_submit_id,
                              self.problem.raw_problem.problem_id,
                              self.language,
                              self.user.raw_user.nickname,
                              self.code,
                              self.problem.raw_problem.time_limit,
                              self.problem.raw_problem.memory_limit)
        # 更新相关字段
        self.status = result['result']
        self.code_length = result['codeLength']
        self.memory = result['take_memory']
        self.run_time = result['take_time']
        # 更新相关用户和题目的各种计数
        self.problem.all_submit += 1
        self.user.all_submit += 1
        if self.status == "System Error":
            self.problem.se += 1
            self.user.se += 1
        if self.status == "Runtime Error":
            self.problem.re += 1
            self.user.re += 1
        if self.status == "Compile Error":
            self.problem.ce += 1
            self.user.ce += 1
        if self.status == "Time Limit Exceeded":
            self.problem.tle += 1
            self.user.tle += 1
        if self.status == "Memory Limit Exceeded":
            self.problem.mle += 1
            self.user.mle += 1
        if self.status == "Wrong Answer":
            self.problem.wa += 1
            self.user.wa += 1
        if self.status == "Accepted":
            self.problem.ac += 1
            self.user.ac += 1
        if self.status == "Presentation Error":
            self.problem.pe += 1
            self.user.pe += 1
        # 入库
        self.problem.save()
        self.user.save()
        self.save()
