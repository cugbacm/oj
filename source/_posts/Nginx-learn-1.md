title: Nginx学习(1)
date: 2014-07-23 03:38:56
tags: [Nginx]
categories: Nginx
toc: true
---
1. 安装
`sudo apt-get install nginx`

2. 查看nginx 状态
`ps -ef | grep nginx`
其中 master是主进程号

3. 查看nginx.conf是否配置正确
`nginx -t -c /etc/nginx/nginx.conf`

4. 启动
`nginx -c /etc/nginx/nginx.conf`//就是主进程的路径
还有好几种启动方法。

5. 关闭
`kill -QUIT 主进程号`
或者`pkill -9 nginx`
主进程号可以通过步骤2查到。

6. 重启
`/usr/sbin/nginx -s reload`

7. 查看版本
`nginx -v`