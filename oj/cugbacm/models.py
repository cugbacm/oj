# coding=utf-8
from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    # 用户，很trick的方法自定义了这个user
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # 年级
    session = models.CharField(max_length=20)
    # 专业
    specialty = models.CharField(max_length=100)
    # 手机
    tel = models.CharField(max_length=100)
    # 邮箱
    email = models.EmailField(max_length=100)
    # 昵称
    nickname = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.user)

class Problem(models.Model):
    # 题目id
    problem_id = models.AutoField(primary_key=True)
    # 标题
    title = models.CharField(max_length=100)
    # 时间限制ms
    time_limit = models.IntegerField(default=1000)
    # 内存限制kb
    memory_limit = models.IntegerField(default=65536);
    # AC这道题的数量
    ac = models.IntegerField(default=0);
    # WA这道题的数量
    wa = models.IntegerField(default=0);
    # TLE这道题的数量
    tle = models.IntegerField(default=0);
    # MLE这道题的数量
    mle = models.IntegerField(default=0);
    # PE这道题的数量
    pe = models.IntegerField(default=0);
    # CE这道题的数量
    ce = models.IntegerField(default=0);
    # SE这道题的数量
    se = models.IntegerField(default=0);
    # RE这道题的数量
    re = models.IntegerField(default=0);
    # 题目描述
    description = models.TextField();
    # 输入
    input = models.TextField();
    # 输出
    output = models.TextField();
    # 输入样例
    sampleInput = models.TextField();
    # 输出样例
    sampleOutput = models.TextField();
    # 提示
    hint = models.TextField(default = "", blank=True);
    # 是否可见
    visible = models.BooleanField(default=True)
    # 作者
    author = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return str(self.problem_id) + "\t" + self.title

class Submit(models.Model):
    # 提交id
    submit_id = models.AutoField(primary_key=True)
    # 用户
    user = models.ForeignKey(User, related_name='user_submit')
    # 题目
    problem = models.ForeignKey(Problem, related_name='problem_submit')
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
        ("Presentation Error", "Presentation Error"),
    )
    status = models.CharField(choices=status_option, max_length=100)
    # 所占内存kb为单位
    memory = models.IntegerField()
    # 运行时间ms为单位
    run_time = models.IntegerField()
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
    code_length = models.IntegerField()
    # 提交时间
    date = models.DateTimeField(auto_now_add = True, auto_now=False)
    # 源码
    code = models.TextField()

    def __unicode__(self):
        return str(self.submit_id) + "\t" + str(self.user) + "\t" + str(self.problem.title)
