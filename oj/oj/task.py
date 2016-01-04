from __future__ import absolute_import
from oj.celery import app

@app.task
def judge(submit):
   submit.judge()
