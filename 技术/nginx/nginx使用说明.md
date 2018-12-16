## 安装

```bash
apt-get install nginx
```

The following additional packages will be installed:
  nginx-common nginx-core
Suggested packages:
  fcgiwrap nginx-doc
The following NEW packages will be installed:
  nginx nginx-common nginx-core
Need to get 457 kB of archives.


Nginx的安装目录在 /etc 有，/usr/lib 下有，/usr/sbin下有

主进程在/usr/sbin/nginx
配置文件/etc/nginx/sites-enabled

# nginx的主要操作
启动 停止 平滑重启

如果新的配置文件应用失败，则继续使用旧的配置进行工作

# pid
/run/nginx.pid

# nginx位置
which nginx
whereis nginx

输入命令行： ps -ef | grep nginx 
摁回车，master process 后面的就是 nginx的目录。

# nginx.conf

worker_process表示工作进程的数量，一般设置为cpu的核数
worker_connections表示每个工作进程的最大连接数

listener监听端口

server_name监听域名

location{}是用来为匹配的 URI 进行配置，URI 即语法中的“/uri/”。location  / { }匹配任何查询，因为所有请求都以 / 开头。