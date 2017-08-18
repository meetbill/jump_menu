## jump_menu


<!-- vim-markdown-toc GFM -->
* [下载安装](#下载安装)
* [配置](#配置)
    * [配置登陆信息](#配置登陆信息)
    * [设置密钥登陆远端机器](#设置密钥登陆远端机器)
* [使用](#使用)
    * [日常跳转](#日常跳转)
    * [查看 IP 信息](#查看-ip-信息)
    * [设置登陆某用户时自动执行此程序](#设置登陆某用户时自动执行此程序)
* [运维](#运维)
    * [安装目录](#安装目录)
    * [小提示](#小提示)

<!-- vim-markdown-toc -->

## 下载安装

Install

```
#git clone https://github.com/BillWang139967/jump_menu.git
#cd jump_menu
#sh Install.sh
```

## 配置

### 配置登陆信息

可以执行下 `ww` 生成模板文件

~/.hostlist.cfg

```
[test1]               # 名称
description=test1     # 描述
hostname=192.168.1.220# IP
username=root         # 用户名
hostport=22           # 端口

[test2]               # 名称
description=test1     # 描述
hostname=192.168.1.220# IP
username=root         # 用户名
hostport=22           # 端口
```
### 设置密钥登陆远端机器

[设置密钥登陆方法](https://github.com/BillWang139967/op_practice_book/blob/master/doc/Linux/base.md#%E5%9F%BA%E4%BA%8E%E5%AF%86%E5%8C%99%E7%9A%84%E5%AE%89%E5%85%A8%E9%AA%8C%E8%AF%81%E9%80%9A%E8%AE%AF%E5%8E%9F%E7%90%86)

## 使用

### 日常跳转

```
#ww
```

### 查看 IP 信息

```
#ww -h
```
### 设置登陆某用户时自动执行此程序

```
切换为特定用户
#echo "ww" >> ~/.bashrc
```

## 运维

### 安装目录

```
/opt/ssh_menu/
```
### 小提示

当使用非 22 端口登陆，同时想使用密钥进行登陆时，分发公钥时使用如下方法
```
ssh-copy-id -i ~/.ssh/id_rsa.pub "-p 20022 test@192.168.3.2"
```

