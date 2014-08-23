title: 基于Github的Git应用
date: 2014-07-12 0:52:27
tags: [Git]
categories: Git
toc: true
---
## 创建Github账号
## 创建托管于Github的仓库
## 创建SSH密钥
在Git命令行窗口中输入：
`ssh-keygen -t rsa -C "your_email"`
完成之后，在`~/.ssh`文件夹中有两个文件，`id_rsa`和`id_rsa.pub`,其中`id_rsa`是私钥，`id_rsa.pub`是公钥。
把`id_rsa.pub`里面的东西全部复制下来，然后贴到github的帐号里。
在`account settings -> ssh keys -> add ssh key`，就可以了。
测试：
`ssh -T git@github.com`
出现下面的话就证明连接上了。  
```
Warning: Permanently added the RSA host key for IP address '192.30.252.131' to the list of known hosts.  
Hi yourname! You've successfully authenticated, but GitHub does not provide shell access.  
```
## 设置`username` , `email`
```
git config --global user.name "your name"  
git config --global user.email "your_email@youremail.com"  
```

## 更新日志
- 2014年08月23日 重新整理，等待详细补充。