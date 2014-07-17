title: Git的安装和简单操作
date: 2014-07-07 13:07:07
tags: [Git]
categories: Git
toc: true
---

# 1. 注册一个github帐号。
# 2. 创建一个仓库。
# 3. 安装git
`sudo apt-get install git`
# 4. 创建ssh
`ssh-keygen -t rsa -C "your_email"`
一路按回车就行了。
完成之后，在`~/.ssh`文件夹中有两个文件，`id_rsa`和`id_rsa.pub`,其中`id_rsa`是私钥，`id_rsa.pub`是公钥。
把`id_rsa.pub`里面的东西全部复制下来，然后贴到github的帐号里。
在`account settings/ssh keys/add ssh key`，就可以了。
# 5. 测试连接。
`ssh -T git@github.com`
出现下面的话就证明连接上了。  
```
Warning: Permanently added the RSA host key for IP address '192.30.252.131' to the list of known hosts.  
Hi kdqzzxxcc! You've successfully authenticated, but GitHub does not provide shell access.  
```
# 6. 设置`username` , `email`
```
git config --global user.name "your name"  
git config --global user.email "your_email@youremail.com"  
```

# 7. `git clone`
把代码从github上扒下来。
每个仓库都有个 `HTTP clone URL` .
直接 `get clone HTTP clone URL` 就可以了。
比如，`git clone https://github.com/kdqzzxxcc/antry.git`

# 8. `git push`
把本地代码上传。
比如我们已经把`antry`这个库扒下来了，现在修改了`test.txt`里面的东西，然后要上传。
```
cd antry/  
vim test.txt   
git add .  
git commit -m "another"  
git push  
(输入帐号密码就完成了。)  
```
# 9. Git操作还有很多，请自行百度。