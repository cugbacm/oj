title: python 学习
date: 2014-08-07 03:40:00
categories: Python
toc: true
---
一、在linix在使用python

1、在linux下一般都安装了python,只需在终端中输入 python 即可，若出现

这样的版本信息，说明python已经安装。
2、安装编辑器vim

如果您的系统中没有安装vim，安装vim的方法是，即在root权限下输入`apt-get install vim`

3、经过以上三步,下面可以用vim编写python了。按Ctrl+D键退出root权限。下面举例用vim写一句python代码，      测试一下。

输入`vim test.py` //创建python文件test.py,并进入到vim编辑器

在vim编辑器中,按 i 键进入到文件的插入状态，现在可以在vim编辑器里编写python了。编写代码如下,

        

然后按Esc键退出插入状态,

输入`(:wq!)`按Enter键,就会保存test.py文件并退出vim。

输入`python test.py`如下，按Enter键，就可以得到运行结果了

     

   

python的相关语法将在本周内学习完成。



二、在windows下使用python

访问Python.org/download，可以下载到python的最新版本，在wondows系统中IDLE就是编辑器。

选择使用`IDLE`程序。IDLE是集成开发环境的缩写。点击`开始->程序->Python 2.3->IDLE(Python GUI)。`

（1)可以再上面直接写语句:print ("hello world!")  按enter键后即可执行。

（注意：3.4.1版本为print ("hello world!")；2.x.x版本为print "hello world!"因版本差异语法略有不同）

(2)也可以打开一个.py文件执行。

    

python基础语法学习：http://sebug.net/paper/python/
上周已经将python基础语法了解，学习过程中的例子全部敲了一遍或两遍。基本知道怎么使用，但对于精确，熟练运用还有很大差距。
当然，在学习过程中还几个遗留问题，待解决后再贴到博客中。