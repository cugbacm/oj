title: Python(1)
date: 2014-08-07 03:30:30
categories: Python
toc: true
---
第一次接触Python，看了一下那个《简明Python教程》前8章和第九章的一点，学习了一下基本的知识，简单总结一下：

# 1：Python的特色：            
简单，易学，免费、开源，高层语言，可移植性，解释性，面向对象，可扩展性，可嵌入性，丰富的库

# 2：Python的安装：
Linux系统下面，在很多情况下已经安装了python是不需要安装的，可以使用：python -V查看是否安装了python,如果显示了版本的话就证明已经安装了，没有的话可以直接使用
apt-get命令安装

# 3：准备工作：
主要就是选择编辑器，在linux下，vim就是一个很好的编辑器（[具体用法请点击此处](http://cugbacm.github.io/oj/2014/07/23/Linux-learn-diary-3/)）。然后就是学习一下python的创建过程和运行方法。比如Hello World程序的完整过程如下：

## 3.1：选择编辑器，我选择vim
```
***@ubuntu:~/Python$ vim
```
进入如下界面（可能会有不同）：
```
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                              VIM - Vi IMproved                                
~                                                                               
~                                 版本 7.3.429                                  
~                           维护人 Bram Moolenaar 等                            
~              修改者 pkg-vim-maintainers@lists.alioth.debian.org               
~                       Vim 是可自由分发的开放源代码软件                        
~                                                                               
~                              赞助 Vim 的开发！                                
~                输入  :help sponsor<Enter>    查看说明                         
~                                                                               
~                输入  :q<Enter>               退出                             
~                输入  :help<Enter>  或  <F1>  查看在线帮助                     
~                输入  :help version7<Enter>   查看版本信息                                                        
      
```

## 3.2：进入编辑模式并编写代码保存：
按i，效果如下：
```
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                              VIM - Vi IMproved                                
~                                                                               
~                                 版本 7.3.429                                  
~                           维护人 Bram Moolenaar 等                            
~              修改者 pkg-vim-maintainers@lists.alioth.debian.org               
~                       Vim 是可自由分发的开放源代码软件                        
~                                                                               
~                              赞助 Vim 的开发！                                
~                输入  :help sponsor<Enter>    查看说明                         
~                                                                               
~                输入  :q<Enter>               退出                             
~                输入  :help<Enter>  或  <F1>  查看在线帮助                     
~                输入  :help version7<Enter>   查看版本信息                     
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
-- 插入 --      
```
下面显示插入模式时就可以写代码了，编辑完成之后如下：
```
#!/usr/bin/python
#Filename helloworld.py

print 'Hello World'


```
然后先返回Esc在按:进入命令模式，给文件命名：
```
:file helloworld.py
```
回车之后，按:wq保存并退出vim
这时候使用ls查看当前目录就会发现helloworld.py已经存在了：
```
break.py         func_doc.py    helloworld.py     mymodule.pyc   using_name.pyc
continue.py      func_param.py  mymodule_demo.py  using_list.py  using_sys.py
func_default.py  function1.py   mymodule.py       using_name.py
```

## 3.3：执行helloworld.py
```
zhaolong@ubuntu:~/Python$ python helloworld.py
Hello World
我们会发现界面输出了Hello World,这样Hello World就创建成功了，也是一个典型Python的过程。
```

# 4：基本概念：
主要就是一些基本类型的说明：数，字符串，变量，对象等等
其中有一个就是逻辑行与物理行的区别与联系：
物理行就是我们看到的一行行的形式，而逻辑行是python执行程序看到的一行行的形式。这两者可以有的关系有：1对n, n对1，1对1

# 5：运算符：
主要就是介绍对应的运算符的一些用法，那个列表蛮好的，可以copy过来：
|运算符|名称|说明|例子|
|-|-|-|-|
|`+`	|加|	两个对象相加|	3 + 5得到8。'a' + 'b'得到'ab'。|
|`-`	|减	|得到负数或是一个数减去另一个数|	-5.2得到一个负数。50 - 24得到26。|
|`*`|	乘|	两个数相乘或是返回一个被重复若干次的字符串|	2 * 3得到6。'la' * 3得到'lalala'。|
|`**`	|幂	|返回x的y次幂|3 ** 4得到81（即3 * 3 * 3 * 3）|
|`/`|	除|	x除以y	|4/3得到1（整数的除法得到整数结果）。4.0/3或4/3.0得到1.3333333333333333|
|`//`	|取整除|	返回商的整数部分|	4 // 3.0得到1.0|
|`%`|	取模|	返回除法的余数|	8%3得到2。-25.5%2.25得到1.5|
|`<<`|	左移|	把一个数的比特向左移一定数目（每个数在内存中都表示为比特或二进制数字，即0和1）|	2 << 2得到8。——2按比特表示为10|
|`>>`|	右移|	把一个数的比特向右移一定数目|11>>1得到5。——11按比特表示为1011，向右移动1比特后得到101，即十进制的5。|
|`&`	|按位与|	数的按位与|	5 & 3得到1。|
|`|`|	按位或|	数的按位或|	5 | 3得到7。|
|`^`|	按位异或|	数的按位异或|	5 ^ 3得到6|
|`~`|	按位翻转|	x的按位翻转是-(x+1)	~5得到-6。|
|`<`	|小于|	返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。|	5 < 3返回0（即False）而3 < 5返回1（即True）。比较可以被任意连接：3 < 5 < 7返回True。|
|`>`|	大于|	返回x是否大于y|	5 > 3返回True。如果两个操作数都是数字，它们首先被转换为一个共同的类型。否则，它总是返回False。|
|`<=`|	小于等于|	返回x是否小于等于y|	x = 3; y = 6; x <= y返回True。|
|`>=`	|大于等于|	返回x是否大于等于y|	x = 4; y = 3; x >= y返回True。|
|`==`	|等于|	比较对象是否相等|	x = 2; y = 2; x == y返回True。x = 'str'; y = 'stR'; x == y返回False。x = 'str'; y = 'str'; x == y返回True。|
|`!=`	|不等于|	比较两个对象是否不相等|	x = 2; y = 3; x != y返回True。|
|`not`|	布尔“非”|	如果x为True，返回False。如果x为False，它返回True。|	x = True; not x返回False。|
|`and`|	布尔“与”|	如果x为False，x and y返回False，否则它返回y的计算值。|	x = False; y = True; x and y，由于x是False，返回False。在这里，Python不会计算y，因为它知道这个表达式的值肯定是False（因为x是False）。这个现象称为短路计算。|
|`or`	|布尔“或”|	如果x是True，它返回True，否则它返回y的计算值。|	x = True; y = False; x or y返回True。短路计算在这里也适用。|

当然，其他的和c++之类的有点像，在我们像改变运算的优先级的时候就必须使用括号来处理，一般的都是按照普通的顺序执行，就统计从左往右等等。比如：
```
 #!/usr/bin/python
# Filename: expression.py

length = 5
breadth = 2
area = length * breadth
print 'Area is', area
print 'Perimeter is', 2 * (length + breadth) 
```
这里就是我们需要先计算加法，后计算乘法，所以改变使用括号

# 6：控制流：
这一章就是讲一下for,if,while等等的用法，整体上和c/c++差不多，主要是细节的问题：
注意：6.1：elif和else从句都必须在逻辑行结尾处有一个冒号，下面跟着一个相应的语句块
            6.2：在Python中没有switch语句。你可以使用if..elif..else语句来完成同样的工
            6.3：可以在while循环中使用一个else从句。 
            6.4：如果你从for或while循环中 终止 ，任何对应的循环else块将不执行。
            
**for的例子:**
```
zhaolong@ubuntu:~$ cat for.py
#!/usr/bin/python
#Filename: for.py

for i in range(1,5):
	print i
else:
	print 'The for loop is over'
```

**if的例子：**
```
zhaolong@ubuntu:~$ cat if.py
#!/usr/bin/python
#Filename: if.py

number = 23
guess = int(raw_input('Enter an integer:'))

if guess == number:
	print 'Congratulations'
elif guess < number:
	print 'No smaller'
else:
	print 'No heigher'

print 'Done'
```

# 7：函数：
这一章主要是介绍在python中如何构造函数：
在Python中创建函数是使用def定义的，例如：
```
zhaolong@ubuntu:~/Python$ cat function1.py
#!/usr/bin/python
#Filename : function1.py

def sayHello():
	print 'helloWOrld!!!'

sayHello()

```
局部变量/形参和实参的区别和c/c++类似，不再赘述
全部变量使用global即可
默认参数值：
这个也就是我们在传参的时候，如果有的参数想使用默认的话可以直接在函数声明的时候赋值，这样当我们不传参的时候就是使用默认值：
```
zhaolong@ubuntu:~/Python$ cat func_default.py
#!/usr/bin/python
#Filename:func_default.py

def say(message, times = 1):
	print message*times

say('hello')
say('world',5)

```
关键参数就是说在使用函数的时候可以直接明确给哪一个变量赋值，这样有时可以不用考虑参数的位置问题
DocStrings：这是一个在函数中写函数解释的重要方法，可以doc产出，在以后的处理中是一个很重要的方法：
```
zhaolong@ubuntu:~/Python$ cat func_doc.py
#!/usr/bin/python
#Filename : func_doc.py

def printMax(x,y):
	'''Print ths maximun of two numbers

	The two values must be integers.'''
	x = int(x)
	y = int(y)
	if x > y:
		print x, 'is maximum'
	else:
		print y, 'is maximum'

printMax(3,5)
print printMax.__doc__

```

# 8：模块：
第7章讲的是在一个python程序中，写函数（重用代码）。这部分代码只能在一个程序中重用，而模块就是实现在多个程序中代码的重用：
当我们编写.py文件的时候，在后面的程序中我们就可以直接使用了。比如：
先创建一个.py文件：
```
 #!/usr/bin/python
# Filename: mymodule.py

def sayhi():
    print 'Hi, this is mymodule speaking.'

version = '0.1'

# End of mymodule.py 
```
然后在第二个python中调用：
```
 #!/usr/bin/python
# Filename: mymodule_demo.py

import mymodule

mymodule.sayhi()
print 'Version', mymodule.version 
```
然后执行第二个python之后，我们就会发现如下结果：
```
$ python mymodule_demo.py
Hi, this is mymodule speaking.
Version 0.1 
```
这样就成功的在一个程序中引用了另一个程序。
在执行完第二个程序之后，我们会发现在目录下面产生了一个.pyc文件：
```
mymodule.pyc
```
这个是加快了程序的执行速度的。

# 9：数据结构：
现在只看了一个列表的：
把这个例子放上来，应该就懂得差不多了：
```
zhaolong@ubuntu:~/Python$ cat using_list.py
#!/usr/bin/python
#Filename:using_list.py

#This is mu shopping list
shoplist = ['apple','mango','carrot','banana']

print 'I hava', len(shoplist), 'items to purchanase.'

print 'These items are:', 
for item in shoplist:
	print item,

print '\nI also hava to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist

print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is',shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bougnt the', olditem
print 'My shopping list is now', shoplist
```
其实就是使用[]存放目标对象，使用各种方法，比如append,del等对其操作。
List是可以进行添加、删除或是搜索列表中的项目的。与后面看到的元组是不一样的。
后面的还在看.....


