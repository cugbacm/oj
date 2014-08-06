title: RabbitMQ(2)
date: 2014-08-07 03:28:00
categories: RabbitMQ
toc: true
---
**上一次安装了RabbitMQ并成功创建了vhost和user，但是生产和消费的过程还没有完成，这次主要调了一下这个过程。**

上次主要的问题是没有实现过程代码的编写保存，其实也就是Python程序，这两天看了一下Python的基本知识，完成了基本的Hello World的生产消费：
# 编写
## 1.生产send.py：
进入vim，编写生产进程
```
!/usr/bin/env python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
```
**过程**：先和RabbitMQ server建立连接，localhost代表的是本机，如果要连接到其它主机，使用对应的主机地址就OK
；声明队列hello；由于消息不能直接传递到消息队列当中去，所以需要一次exchange，这里使用默认的交换
'',routing_key为队列的名字；然后在关闭连接。

## 2.消费receive.py
进入vim,编写消费进程
```
!/usr/bin/env python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
print ' [*] Waiting for messages. To exit press CTRL+C'
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
channel.basic_consume(callback,queue='hello',no_ack=True)
channel.start_consuming()
```
**过程**：建立连接；声明队列，这里声明的原因是我们不知道预先存在的队列是什么，所以我们就确定化我们的目标
消费队列就是我们前面缩写的send.py里面的队列hello；然后建立我们的消费方法callback；然后声明消费的
对象队列是hello队列；然后启动。

# 测试

测试的时候，首先启动生产进程send.py：
```
$ python send.py
 [x] Sent 'Hello World!'
```

然后我们会显示生产的标识消息：[x] Sent 'Hello World!'
生产进程每执行一次生产就停止了。
然后再启动消费进程：
```
$ python receive.py
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received 'Hello World!'
```

这里我们就会发现在Received后面出现了我们生产进程中发出的信息'Hello World!',这样便完成了一次生产消费过程。
也可以打开两个终端，在其中一个终端上一直执行生产进程，我们会发现在另一个终端上会一直显示我们的消费标识
信息，即边生产边消费。

后面第二部分的就是多个消费worker()，还在看.....


