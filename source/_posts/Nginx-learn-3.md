title: Nginx学习(3)
date: 2014-07-23 03:46:57
tags: [Nginx]
categories: Nginx
toc: true
---
之前一直以为OJ上不了了，后来才发现是要在ip后面加/index/login才能上。
感觉太麻烦了，就想直接ip登录。
实现过程试了很多种方法。
# 一、设置默认首页
```
location / {
   root /xxx/xxx
   index index.html index.htm
}
```
当访问ip时，会请求/xxx/xxx 里面的index.html或者index.htm，并产生响应。
root 后面是index.html index.htm的路径，匹配规则是当index.html没有的时候，继续匹配index.htm。
这样之后发现不行，问了朱老板才知道OJ的页面都是要经过django渲染之后才能显示的。

# 二、
```
location /{
include uwsgi_params;
uwsgi_pass 127.0.0.1:8077;
}
```
这是django的location，这样的配置可以是的所有的子网页都经过django的渲染。
然后我发现其实把这个放在/index 这一层就可以了，因为都是这种形式的/index/xxx。
那么我们直接做个重定向就可以了。
```
location / {
rewrite ^ ip/index/login ;
}

location /index{
include uwsgi_params;
uwsgi_pass 127.0.0.1:8077;
}
```
此时我们直接访问ip，即跳转到index/login页面，但是登录之后点其他页面却重新跳回了index/login页面。
比如点problemList ,他就跳回了index/login。
这是因为在server里面没有匹配到/index/problemList。所以根据匹配的规则他会匹配到location /{}上， 那么就跳回到index/login。

# 三、
这个问题也很好解决，我们只要不让他在index/problemList的时候去匹配到location / {}就可以了。
实现办法就是
```
location = / {
rewrite ^ ip/index/login ;
}
```
因为location / {}是匹配所有以/开头的查询。
而location = / {}则只匹配以/ 开头的查询，那么当查询index/problemList的时候，就去匹配location/index{}了。
这样就完美解决了以上问题。

# 四、
突然发现其实不需要将django的配置放到/index
这样就可以了
```
location = / {
rewrite ^ ip/index/login ;
}

location /{
include uwsgi_params;
uwsgi_pass 127.0.0.1:8077;
}
```

# 五、
location的一些匹配规则
```
location = / {
 # 只匹配 / 查询。
 
}location / {
 # 匹配任何查询，因为所有请求都已 / 开头。但是正则表达式规则和长的块规则将被优先和查询匹配。
 
}location ^~ /images/ {
 # 匹配任何已 /images/ 开头的任何查询并且停止搜索。任何正则表达式将不会被测试。
 
}location ~* .(gif|jpg|jpeg)$ {
 # 匹配任何已 gif、jpg 或 jpeg 结尾的请求。
 
}location ~* .(gif|jpg|swf)$ {
  valid_referers none blocked start.igrow.cn sta.igrow.cn;
  if ($invalid_referer) {
  #防盗链
  rewrite ^/ http://$host/logo.png;
  }
}
location ~* .(js|css|jpg|jpeg|gif|png|swf)$ {
if (-f $request_filename) {
   #根据文件类型设置过期时间
   expires    1h;
   break;
}
}
location ~* .(txt|doc)${ 
 #禁止访问某个目录
    root /data/www/wwwroot/linuxtone/test;
    deny all;
}
```