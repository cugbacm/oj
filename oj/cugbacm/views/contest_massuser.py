#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cugbacm.models import User, Submit, Problem, Contest, ContestSubmit, UserContestMap
from django.http import HttpResponse, HttpResponseRedirect
import sys
import xlrd
import xlwt
import string,random

@csrf_exempt
#直接在url里添加参数
def production(request):
  contest_id = str(request.GET.get('id'))
  contest_name = str(request.GET.get('name'))
#addr 这里需要输入路径，可以与contest_name对应
  data = xlrd.open_workbook('/home/cugbacm/oj/oj/cugbacm/views/demo.xls')

  file = xlwt.Workbook(encoding='utf-8')
  wtable = file.add_sheet('sheet1', cell_overwrite_ok=True)

  add_ncols = 2
  table = data.sheets()[0]

#姓名 手机号 邮箱 年级 账号 密码
  try:
    for rownum in range(table.nrows):
      nickname = ''
      tel = ''
      email = ''
      session = ''
      for colnum in range(table.ncols):
        s = table.cell(rownum, colnum).value
#这里xlrd在导入的时候默认将整型转换为浮点型，所以导出时得转换下
        if type(s) == float and s == int(s):
          s = int(s)
        s = str(s)
        wtable.write(rownum, colnum, s)
        if rownum > 0 and colnum == 0:
          nickname = s
        if rownum >0 and colnum == 1:
          tel = s
        if rownum >0 and colnum == 2:
          email = s
        if rownum >0 and colnum == 3:
          session = s
      if rownum > 0:
        userID = 'team'+str(rownum)
        password = str(getPwd())
        User(
              userID = userID,
              password = password,
              session = session,
              tel = tel,
              email = email,
              nickname = nickname).save()

        UserContestMap(
              userID = userID,
              contestID = contest_id).save()

      for colnum2 in range(add_ncols):
        if rownum == 0 and colnum2 == 0:
          wtable.write(rownum, 4+colnum2, '账号')
        if rownum == 0 and colnum2 == 1:
          wtable.write(rownum, 4+colnum2, '密码')
        if rownum > 0 and colnum2 == 0:
          wtable.write(rownum, 4+colnum2, userID)
        if rownum > 0 and colnum2 == 1:
          wtable.write(rownum, colnum+add_ncols, password)
    file.save('/home/cugbacm/oj/oj/cugbacm/views/wdemo.xls')
    return HttpResponse('yes')
  except:
    return HttpResponse('no')

def delete(request):
  data = xlrd.open_workbook('/home/cugbacm/oj/oj/cugbacm/views/wdemo.xls')
  table = data.sheets()[0]
#姓名 手机号 邮箱 年级 账号 密码
  try:
    for rownum in range(table.nrows):
      if rownum > 0:
        userid = str(table.cell(rownum, 4).value)
        User.objects.get(userID = userid).delete()
        UserContestMap.objects.get(userID = userid).delete()
    return HttpResponse('yes')
  except:
    return HttpResponse('no')

def getPwd():
  length=8
  seedlower=string.lowercase
  seeddigit=string.digits
  seedupper=string.uppercase
  pwd=pwdd=pwdl=pwdu=''

  countl=random.randrange(1,length-1)
  countu=random.randrange(1,length-countl)
  countd=(length-countl-countu)

  #生成随机的字符
  for l in random.sample(seedlower,countl):
    pwdl+=l
  for u in random.sample(seedupper,countu):
    pwdu+=u
  for d in random.sample(seeddigit,countd):
    pwdd+=d

  #在随机位置出现随机的字符
  seed=pwdl+pwdu+pwdd
  shuffler=random.sample(seed,len(seed))
  pwd="".join(shuffler)
  return pwd
