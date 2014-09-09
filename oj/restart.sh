ps -ef|grep uwsgi|grep -v grep|cut -c 9-15|xargs kill -9
uwsgi -x ~/oj/oj/django_socket.xml 
