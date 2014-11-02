ps -ef|grep celery|grep -v grep|cut -c 9-15|xargs kill -9
nohup python manage.py celeryd -B -D -l info

