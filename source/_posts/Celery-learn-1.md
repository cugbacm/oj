title: Celery学习笔记
date: 2014-08-07 04:13:00
categories: RabbitMQ
toc: true
---
ubuntu系统下安装指令：

## 安装rabbitmq：
```
$ sudo apt-get install rabbitmq-server
```
## 安装celery：
```
sudo easy_install celery
```
注意：这里我开始采用官方文档的指令
```
$ pip install celery
```
不过发现用不了，执行后面的指令提示不能识别。

可以安装rabbit-celery 或者 使用easy_install安装celery

## 创建tasks.py文件
```
from celery import Celery

app = Celery('tasks', broker='amqp://localhost')

@app.task
def add(x, y):
    return x + y
```
## 使用worker启动服务器，如果不启动，会得不到结果，例如官网上出现false的情况。
```
$ celery -A tasks worker --loglevel=info
```
使用以下指令可以显示命令列表
```
$  celery worker --help
```
```
$ celery help
```

## 下面来做个测试：

### 启动celery worker 服务器,启动之后，使用其他终端输入指令，这个终端显示结果。
```
$ celery -A tasks worker --loglevel=info
```
### 输入python,进入python环境
```
>>> from tasks import add
>>> add.delay(4, 4)
```
### 取得结果：
这里还得设置一下tasks.py，使用rabbitmq的后台
```
app = Celery('tasks', backend='amqp', broker='amqp://')
```
```
>>> result = add.delay(4, 4)
>>> result.ready()
True
>>> result.get(timeout=1)
8
```

设置app，可以直接在tasks.py中设置，也可调用设置文件。

1.多个设置一起执行 
```
app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
)
```
2. 调用外部文件
```
app.config_from_object('celeryconfig')
```

3.celeryconfig.py
```
BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True
```
4.可以通过一下代码来测试是否出错 
```
$ python -m celeryconfig
```
5.设置优先权和速率 
celeryconfig.py:
```
CELERY_ANNOTATIONS = {
    'tasks.add': {'rate_limit': '10/m'}
}
```
也可以直接在外面设置:
```
$ celery -A tasks control rate_limit tasks.add 10/m
worker@example.com: OK
    new rate limit set successfully
```




