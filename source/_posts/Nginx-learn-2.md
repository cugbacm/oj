title: Nginx学习(2)
date: 2014-07-23 03:42:52
tags: [Nginx]
categories: Nginx
toc: true
---
首先是一些配置。
```
user www-data;
worker_processes 1;
#进程数，一般为CPU总核心数
#pid /var/run/nginx.pid;

#进程文件
pid /home/kdq/nginx/logs/nginx.pid ;

events {
	use epoll;
	#epoll是多路复用IO(I/O Multiplexing)中的一种方式,但是仅用于linux2.6以上内核,可以大大提高nginx的性能    
	worker_connections 1024;
	# multi_accept on;
}
```

以上一般都不用自己配了。了解一下一些优化就可以了。
```
http {
	include /etc/nginx/mime.types;

	default_type application/octet-stream;
	##
	# Basic Settings
	##
        #aotoindex on; #
	sendfile on;
	tcp_nopush on;
 	#防止网络阻塞
	tcp_nodelay on;
	#防止网络阻塞
	keepalive_timeout 65;
	#长连接超时，单位秒
	types_hash_max_size 2048;
	# server_tokens off;

	 server_names_hash_bucket_size 64;
	# server_name_in_redirect off ;

	##
	# Logging Settings
	##
	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;
	
	##
	# Gzip Settings
	##
	gzip on;
	gzip_disable "msie6";
	## Basic reverse proxy server ##
	server {
		#监听端口8080
		listen	8080;
		server_name localhost;
		location /{
			proxy_pass http://202.204.102.161;
                        #现在OJ的内网地址
			proxy_redirect default;
		}
		location /status {
			stub_status on;
			access_log on;
			auth_basic "NginxStatus";
			#allow 192.168.0.113 ;
			auth_basic_user_file /etc/nginx/htpasswd ;#密码文件的路径
		#	设置密码
			#htpasswd文件的内容可以用apache提供的htpasswd工具来产生。
		}
	}
        #server {
        #    listen 8087 ;
        #    server_name localhost;
        #    location / {
        #        root /home/kdq/mytask;
        #       
        #    }

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}
```

上面的service主要实现了一个反向代理，通过访问本机的8080端口，可以访问内网的OJ。算是个小试验。。
主要说一下/status。
通过/status，我们可以查看nginx的状态。
主要说一下配置，allow ip，这是限制ip登录。
```
auth_basic_user_file /etc/nginx/htpasswd   
```

这是通过用户名密码登录。
用户名密码就存在htpasswd这个文件里。
格式是user:passwd ,密码用crypt加密。
直接用命令mkpasswd+密码,得到的密码就是加密后的。
```
kdq@ubuntu:/etc/nginx$ sudo mkpasswd 
密码： 
OEThvZTvhXfvE
```

然后把这个密码复制到那个文件里，按照上述格式就可以了。
status:
```
Active connections: 1 
server accepts handled requests
 2 2 4 
Reading: 0 Writing: 1 Waiting: 0 
```

更多资料请参考：<http://wiki.nginx.org/Main>
这个博客很好：<http://blog.sina.com.cn/openresty>