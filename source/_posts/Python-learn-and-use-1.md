title: python 学习笔记
date: 2014-08-07 04:03:00
categories: Python
toc: true
---
# 1.字符串

## 1.1
不同于 C 字符串，Python 字符串不可变。向字符串文本的某一个索引赋值会引发错误:
```
>>> word[0] = 'x'
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: 'str' object does not support item assignment
>>> word[:1] = 'Splat'
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: 'str' object does not support slice assignment
```
## 1.2 
支持word[2,4], word[-4,-2]格式，负数是从右向左数的。而且，负索引切片越界会被截断，不要尝试将它用于单元素（非切片）检索:
```
>>> word[-10]    # error
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
IndexError: string index out of range
```
#1.3  
字符串可以使用encode()进行编码
```
>>> "Äpfel".encode('utf-8')
b'\xc3\x84pfel'
```
# 2.符合数据类型 
## 2.1 
List可赋值和插入
```
>>> a[1:1] = [1,2]
>>> a[1:1]
[]
>>> a[1:1] = [2]
>>> a
[1, 2, 2]
```
## 2.2 
List可嵌套List

## 2.3 
print输出时会自动换行，如果不想换行，可以加上 end =''，并且导入print_function
```
>>> from __future__ import print_function
>>> for x in range(0,10):
...   print (x, end='')
... 
0123456789>>> 
```

## 2.4 
同一个语句块中的语句块必须缩进同样数量的空白，而且至少要有一个空格，否则会报错。
```
>>> for x in range(0,10):
... print (x)
  File "<stdin>", line 2
    print (x)
        ^
IndentationError: expected an indented block
```
# 3. python流程控制
## 3.1
```
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```
逆序的话，用reversed嵌套
在不同方面 range() 函数返回的对象表现为它是一个列表，但事实上它并不是。 当你迭代它时，它是一个能够像期望的序列返回连续项的对象；但为了节省空间，它并不真正构造列表。

我们称此类对象是 可迭代的 ，即适合作为那些期望从某些东西中获得连续项直到结束的函数或结构的一个目标（参数）。 我们已经见过的 for 语句就是这样一个 迭代器 。 list() 函数是另外一个（ 迭代器），它从可迭代（对象）中创建列表:

有一点奇怪的事：
 官方文档对于print (range(5))和实际操作不一致
```
 >>> print(range(10))
range(0, 10)
>>> range(5)
[0, 1, 2, 3, 4]

```
代码块缩进必须相同，看这个比较神奇的例子:
```
>>> for n in range(2,10):
...   for x in range(2,n):
...     if n%x == 0:
...        print(n, 'equals', x, '*', n//x)
...        break
...   else :
...     print(n,'is a prime number')
... 
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
这里的else是和for缩进相同所以，一旦执行了else，就不会再执行for了。

## 3.2 pass什么都不做

## 3.3 定义函数

关键字 def 引入了一个函数定义 。在其后必须跟有函数名和包括形式参数的圆括号。函数体语句从下一行开始，必须是缩进的。
函数 调用 会为函数局部变量生成一个新的符号表。 确切的说，所有函数中的变量赋值都是将值存储在局部符号表。 变量引用首先在局部符号表中查找，然后是包含函数的局部符号表，然后是全局符号表，最后是内置名字表。 因此，全局变量不能在函数中直接赋值（除非用global 语句命名），尽管他们可以被引用。
函数引用的实际参数在函数调用时引入局部符号表，因此，实参总是 传值调用 （这里的 值 总是一个对象 引用 ，而不是该对象的值）。[1] 一个函数被另一个函数调用时，一个新的局部符号表在调用过程中被创建。

一个函数定义会在当前符号表内引入函数名。 函数名指代的值（即函数体）有一个被 Python 解释器认定为 用户自定义函数 的类型。 这个值可以赋予其他的名字（即变量名），然后它也可以被当做函数使用。 这可以作为通用的重命名机制.

## 3.4 函数中的默认值
```
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```
输出5，默认值只被赋值一次。这使得当默认值是可变对象时会有所不同，比如列表、字典或者大多数类的实例。例如，下面的函数在后续调用过程中会累积（前面）传给它的参数:
```
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```
这将输出:
```
[1]
[1, 2]
[1, 2, 3]
```
如果你不想让默认值在后续调用中累积，你可以像下面一样定义函数:  
```
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
赋值的位置不一样，在函数体内部赋值，就不会累积了。
可变参数列表：
```
>>> def concat(*args, sep="/"):
...    return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```
最后我把sep放在函数体内部就可以搞定了，仔细想想，如果输入一个数组的话，sep可能就会被最后一个元素覆盖，再没有使用关键字的情况下。

**参数的拆分：**

用`*`能把列表拆分，用`**`能把字典拆分
```
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```
```
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

**函数的嵌套，匿名函数Lambda**
```
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

# 7.输入和输出 
## 7.1函数 open() 返回文件对象，通常的用法需要两个参数： `open(filename, mode)`。

`>>> f = open('/tmp/workfile', 'w')`
第一个参数是一个标识文件名的字符串。第二个参数是由有限的字母组成的字符串，描述了文件将会被如何使用。可选的 模式 有：

`'r'` ，此选项使文件只读；

`'w'` ，此选项使文件只写（对于同名文件，该操作使原有文件被覆盖）；

`'a'` ，此选项以追加方式打开文件；

`'r+'` ，此选项以读写方式打开文件； 
模式 参数是可选的。如果没有指定，默认为 'r' 模式。

在 Windows 平台上， 'b' 模式以二进制方式打开文件，所以可能会有类似于 'rb' ， 'wb' ， 'r+b' 等等模式组合。Windows 平台上文本文件与二进制文件是有区别的，读写文本文件时，行尾会自动添加行结束符。这种后台操作方式对 ASCII 文本文件没有什么问题，但是操作 JPEG 或 EXE 这样的二进制文件时就会产生破坏。在操作这些文件时一定要记得以二进制模式打开。在 Unix 上，加一个 'b' 模式也一样是无害的，所以你可以一切二进制文件处理中平台无关的使用它。

## 7.2在文本文件中（那些没有使用 b 模式选项打开的文件），只允许从文件头开始计算相对位置（使用 seek(0, 2) 从文件尾计算时就会引发异常）。




