#oj2.0
oj2.0是由一群大神学长发起的、几个弱菜学长实现的Online Judge系统。（请允许我做一个悲伤的表情）
oj2.0基于linux系统（测试环境ubuntu12.04-server-64），目前与老OJ对比还差很多功能，例如user搜索、比赛模块、about us等。已经工作的学长们精力有限，所以诚邀各位来继续搞一搞我们的oj2.0，整体架构已经搭建起来了，往里面填就可以了。
##预热
oj2.0虽然很渣，不过对于本科阶段的大家应该算是一个不错的试验品，如果整个OJ搞懂的话，你会学到linux基础、nginx服务器搭建和使用、django web开发、js、html、python、数据库应用、rabbitMQ+celery消息异步传递架构，足够拿一个好offer了。（简历上可以这么写，具有linux系统下开发经验、熟练使用python、shell等脚本语言、了解nginx服务器的使用、有django框架下的web开发经验balabala……秒杀90%的acmer没问题）。当然，上面都是尚未解锁的成就，如何解锁上述成就：
  1. 看看linux入门书籍，比如鸟哥私房菜，学会mkdir、chmod、cd、ll、vim等一些基础命令、了解linux文件系统、权限系统，会在命令行下使用linux系统就可以了。
  2. django框架，网上有中文教程和视频教程，如果没有MVC经验的话，入门需要一段时间，请坚持。
  3. python学习，相信大家已经有了一两年的c++使用时间，学语言的速度应该很快，python学习应该不成问题。
  4. 前端学习，w3c+bootstrap，你们懂得。
  5. 数据库，计算机、软件专业必修课。
  6. rabbitMQ+celery，考察你们英语的时刻到了，官方文档都是英文的，如果英语很好，官方文档你会读得得心应手。否则，有道翻译吧，或者看csdn cugb1004101218，最好还是去官网看。
  7. git入门学习。
  8. 这些都可以谷歌百度得到。上述的列表不一定要学完之后再去搞OJ2.0，各个模块可以单独学习，例如你学完python后，可以搞一搞判题内核；学过前端，就直接可以搞一搞我们OJ的web界面了。不要在意这些细节，这块试验田随便搞的（反正也没人用，呵~呵 -_-!）。

##整体架构
    
###架构图
    +--------+         +--------+         +---------------+         +--------+         +--------+
    |  nginx |<------->| django |<------->|rabbitMQ+celery|<------->|  core  |<------->|  data  |
    +--------+         +--------+         +---------------+         +--------+         +--------+
                            ↑
                            |
                            ↓
                       +--------+
                       |  mysql |
                       +--------+
###各个模块
  1. web框架使用的是django，木有接触过的可以自行百度之。主要特点是灵活性、高复用性、与其他组件接口完善且丰富。
  2. web服务器是nginx，一种高性能服务器。
  3. rabbitMQ消息传递中间件，用来传递判题消息至判题内核。
  4. core判题内核，qiang.he负责的，感兴趣的童鞋找他。
  5. data本地题库，放题目数据的。
  6. mysql存oj信息，user、problem、submit等。
  7. 还有个bootstrap没有写到架构图上，这个是一个前端的框架。

##环境搭建
  1. 上述的几个模块，官网都有安装步骤，不赘述。（可能过程比较痛苦会遇到各种坑）
  2. 将代码git下来。
  3. 搞吧。

#各个模块详细文档（有待各位完善） 
##nginx 
###nginx部署 
  1.安装 
  sudo apt-get install nginx  
  2. 查看nginx 状态  
  ps -ef | grep nginx  
  其中 master是主进程号  
  3.查看nginx.conf是否配置正确  
  nginx -t -c /etc/nginx/nginx.conf  
  4.启动  
  nginx -c /etc/nginx/nginx.conf//就是主进程的路径  
  还有好几种启动方法。  
  5.关闭  
  kill -QUIT 主进程号  
  或者pkill -9 nginx  
  主进程号可以通过步骤2查到。  
  6.重启  
  /usr/sbin/nginx -s reload  
  7.查看版本  
  nginx -v  
  注意：以上如果出错，就加sudo即可。  

###nginx配置  
  默认路径 /etc/nginx/nginx.conf  
  oj路径  /usr/local/openresty/nginx/conf/nginx.conf  
  #运行用户    
  user www-data;    
  #启动进程,通常设置成和cpu的数量相等  
  worker_processes  1;  
  #全局错误日志及PID文件  
  error_log  /var/log/nginx/error.log;  
  pid        /var/run/nginx.pid;  
  #工作模式及连接数上限  
  events {  
    use   epoll;               
    #epoll是多路复用IO(I/O Multiplexing)中的一种方式,但是仅用于linux2.6以上内核,可以大大提高nginx的性能  
    worker_connections  1024;#单个后台worker process进程的最大并发链接数  
    # multi_accept on;  
}  
  这里是django的配置，使用django渲染  
  location /{  
  include uwsgi_params; 
  uwsgi_pass 127.0.0.1:8077;  
}  
  匹配/index/login最后一个/后面的内容，如果是problemList则跳转到/index/problemList。  
  location = / {  
  rewrite ^ ip/index/login ;  
}  
###nginx调优  
  
##django
###django部署
1.下载安装django  
方法1： 
pip install Django==1.6.5  
测试是否安装成功
:~$python 
>>>import django  
>>> django.VERSION  
(1, 6, 5, 'final', 0) 
2.方法二： 
    大多数人会考虑从 http://www.djangoproject.com/download/ 下载安装最新的官方发布版。Django 使用了 Python 标准的 distutils 安装法，在 Linux 平台可能包括如下步骤：   
    下载 tar 安装包，其文件名可能会是 Django-0.96.tar.gz 。   
    tar xzvf Django-*.tar.gz 。
    cd Django-* 。  
    sudo python setup.py install 。  

###oj2.0中的模型和模板
###django+uwsgi+nginx部署
##mysql
  ###mysql部署  
  安装mysql-server    
  sudo apt-get install mysql-server  
  常用的指令：  
  1. 修改mysql最大连接数  
    vim my.cnf，增加或修改max_connections=1024     my.cnf默认路径:/usr/bin  
  2.  本机登陆mysql：mysql -u root -p  
  3.  建库：create database oj;  
  4.  改变数据库：use oj;  
  5.  显示数据库：show databases ; 
  6.  显示表： show tables;  
  其他的参考：http://www.cnblogs.com/wuhou/archive/2008/09/28/1301071.html   或者百度  

###django中的mysql接口
  在创建的项目中的settings.py进行修改就行了。
  
##rabbitMQ  
###rabbitMQ部署  
  sudo apt-get install rabbitmq-server  
  测试：    
  参考：http://www.rabbitmq.com/tutorials/tutorial-one-python.html  
  
###rabbitMQ配置  

##celery
###celery部署
###celery+django+rabbitMQ配置

测试+部署：  
  参考：http://blog.csdn.net/dipolar/article/details/22162863  
  
配额：直接从服务器上看吧
  
  
##core
###判题流程
###判题内核对外接口
##前端
###js
###html
###bootstrap

设置vim，实现每次tab自动空4格
参考：http://www.2cto.com/os/201306/217523.html
cd /root
vim .vimrc
复制下面文本
set tabstop=4 
set softtabstop=4 
set shiftwidth=4 
set noexpandtab 
set nu 
set autoindent 
set cindent 


#本来是想将整个架构每个模块都详细写一写，后来考虑到可以交给学弟学妹们找感兴趣的模块边学边记录文档到这里，既能完善我们的文档、又能让学弟学妹们学到对应的知识，所以每个模块的文档有待学弟学妹们来完善了。（其实就是懒，找那么多借口-_-!，期间遇到任何问题联系763687347,一起讨论）
