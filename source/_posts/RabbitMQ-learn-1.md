title: RabbitMQ(1)
date: 2014-07-23 03:46:57
tags: [RabbitMQ]
categories: RabbitMQ
toc: true
---
看了一下RabbitMQ的介绍，主要是一个message queue,即消息队列,一段往消息队列中不断写入信息，而另一端则可以读取信息。主要是用来处理消息的，目前主要是安装了Linux版的RabbitMQ：

# 1:安装erlang
`apt-get install erlang-nox`
# 2:下载安装RabbitMQ安装包
我直接在它的官网上下载的最新版的安装包安装的rabbitmq-server_3.3.4-1_all.deb
# 3:启动
`/etc/init.d/rabbitmq-server start`
# 4:创建一个创建一个vhost
`rabbitmqctl add_vhost /pyhtest`
第一次创建的时候不知道为什么总是创建不了，后来重新敲了一遍又好了
# 5:然后再给这个vhost创建一个用户
`rabbitmqctl add_user pyh pyh1234`
用户名pyh 密码pyh1234
# 6:创建权限
`rabbitmqctl set_permissions -p /pyhtest pyh “.*” “.*” “.*”`
*代表全部权限

后来写了一个send和receive，现在还没有弄好这个发送和消费的过程，再弄......

官网上有详细的样例的介绍说明，比如Hello World！：
<http://www.rabbitmq.com/tutorials/tutorial-one-python.html>