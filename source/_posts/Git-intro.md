title: Git介绍
date: 2014-07-12 0:52:27
tags: [Git]
categories: Git
toc: true
---
## 安装
### Linux下
打开命令行，输入：`apt-get install git`
如果报错：`ubuntu-E:Encountered a section with no Package: header`，则需要更新软件库，输入以下代码：
```
sudo rm /var/lib/apt/lists/* -vf
sudo apt-get update
```
### Windows下
**命令行界面**
可以下载msysGit,  像在Linux上一样使用命令行控制。
**图形化界面**
下载TortoiseGit对msysGit进行配置。这时，鼠标右键菜单会有相应的命令，且显示图形界面。
或者，使用Github提供的客户端——`Github Windows`

## 基本操作
`git clone` 本地克隆远程git版本库
`git init`和`git remote` 手动的版本库更新（两者都是对git的初始化）
`git pull` 从其他版本库更新代码
`git add` 将当前操作加入版本库
`git rm` 删除
`git commit` 提交
`git push` 将本地的代码更新上远程版本库
`git log` 查看历史日志
`git revert` 还原版本

## 更新日志
- 2014年08月23日 重新整理，细节部分有待完善。