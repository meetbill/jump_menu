## Install

Install

```
#git clone https://github.com/BillWang139967/jump_menu.git
#cd jump_menu
#sh Install.sh
```

## 配置

/opt/ssh_menu/hostlist.cfg

```
[test1]               # 名称
description=test1     # 描述
hostname=192.168.1.220# IP
username=root         # 用户名
hostport=22           # 端口
```
### 小提示

当使用非22端口登陆，同时想使用密钥进行登陆时，分发公钥时使用如下方法
```
ssh-copy-id -i ~/.ssh/id_rsa.pub "-p 20022 test@192.168.3.2"
```

## 使用

日常跳转
```
#ww
```
查看IP信息
```
#ww -h
```

## 运维

安装目录
```
/opt/ssh_menu/
```
