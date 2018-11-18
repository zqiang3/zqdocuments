## nginx和uwsgi的关系
nginx相当于是服务器，负责接收请求

uwsgi是服务器和服务端应用程序的通信协议，规定了怎么把请求转发给应用程序和返回

2个基本概念： 
服务器：接收请求，应用程序：处理请求并返回

通信过程： 

客户端发送一个http请求，被nginx服务器接收，nginx服务器将请求转发给uwsgi,uwsgi将请求转发给实现uwsgi协议的应用程序(flask,gunicorn等等)

## 原文

https://blog.csdn.net/guoqingpei/article/details/52749101 