title: git的安装及简单应用
date: 2014-08-07 03:50:00
categories: Git
toc: true
---
1、第一次在root下输入  `apt-get install git` 后提示有错误：`ubuntu-E:Encountered a section with no Package: header`
在网上搜了一下，是因为在软件库中找不到软件包，所以要更新软件库。方法如下：
终端中输入以下两条命令：
```
sudo rm /var/lib/apt/lists/* -vf
sudo apt-get update
```
大约几分钟，执行完了命令之后，软件更新器应该会自动要求更新的，更新便是。
  
2、然后按照以下网址中的内容进行操作即可
http://cugbacm.github.io/oj/2014/07/07/git-install-operation/

git的其他命令还在学习中