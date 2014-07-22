title: git配置和简单使用
date: 2014-07-23 03:37:30
tags: [git]
categories: Git
toc: true
---
# Git安装
## 在windows上安装：可以下载msysGit,  像在Linux上一样使用命令行控制.
如果想实现可视化控制，可再下载TortoiseGit对msysGit进行配置。这时，鼠标右键菜单会有相应的命令，且显示图形界面。
## 在linux上安装：`sudo apt-get install git`

# Git使用
推荐使用教程: <http://www.bootcss.com/p/git-guide/>，来回看这里就知道怎么用了。
GitHub作为远程仓库连接: 连接GitHub

# Git新手贴士
1. Git分为远程仓库(Respository)和本地仓库。多人维护一个项目的话，大家可以共用一个远程仓库。
   个人拉取(pull)远程仓库到本仓库，自己进行修改后, 在(push)推送到远程仓库更新。一般大家喜欢设在GitHub上放远程仓库。
   远程仓库只接受本地仓库push的修改变动。手动修改都是不安全不见意的。
2. 建立本地仓库      `git init "仓库名字"`  。
建立远程仓库的话      `git init --bare "仓库名字.git"`   就可以了。
3. 如果不在GitHub上设立远程仓库。用2中的命令我们可以在自己的服务器上设立远程仓库。这时如果两台机器能进行ssh通信。就本地机器可以使用服务器上的远程仓库   了。
4. 和服务进行ssh通信的配置很简单。先本地生成RSA密钥和公钥，在服务器上的/temp下添加RSA公钥就行了。在git bash上ssh -t  用户名@ip 可以进行尝试和服务器通信(登陆)，如果成功就可以push和pull了。跟在github上配置差不多。
5. 在本地仓库里git config -l查看git配置。如果需要使用远程仓库，需要对本地仓库进行远程仓库服务器设置：git remote add  “服务器名字” 用户名@ip:“远程仓库目录地    址”。或者直接使用clone命令，直接完成本地仓库的新建，服务器添加和pull过程。
6. 在自定义分支里面对代码进行修改，觉得可用稳定后才合并到master分支。
7. 各种维护代码的专业用法欢迎指点。


