## 参考链接

https://www.jianshu.com/p/679dee0a4193

https://blog.csdn.net/a519640026/article/details/76157976

## 几个概念

**WSGI协议**：全称是`Web Server Gateway Interface`，即web服务器网关接口。`WSGI`不是服务器，`python`模块，框架，`API`或者任何软件，只是一种规范，描述`web server`如何与`web application`通信的规范。

**uwsgi：**与`WSGI`一样是一种通信协议，是`uWSGI`服务器的独占协议，用于定义传输信息的类型(`type of information`)，每一个`uwsgi packet`前`4byte`为传输信息类型的描述，与WSGI协议是两种东西，据说该协议是`fcgi`协议的10倍快。

**uWSGI：**是一个`web`服务器，实现了`WSGI`协议、`uwsgi`协议、`http`协议等。

## WSGI协议规范

`WSGI`协议主要包括`server`和`application`两部分：

- `WSGI server`负责从客户端接收请求，将`request`转发给`application`，将`application`返回的`response`返回给客户端；

- `WSGI application`接收由`server`转发的`request`，处理请求，并将处理结果返回给`server`。`application`中可以包括多个栈式的中间件(`middlewares`)，这些中间件需要同时实现server与application，因此可以在WSGI服务器与WSGI应用之间起调节作用：对服务器来说，中间件扮演应用程序，对应用程序来说，中间件扮演服务器。


`WSGI`协议其实是定义了一种`server`与`application`解耦的规范，即可以有多个实现`WSGI server`的服务器，也可以有多个实现`WSGI application`的框架，那么就可以选择任意的`server`和`application`组合实现自己的`web`应用。例如`uWSGI`和`Gunicorn`都是实现了`WSGI server`协议的服务器，`Django`，`Flask`是实现了`WSGI application`协议的`web`框架，可以根据项目实际情况搭配使用。

像`Django`，`Flask`框架都有自己实现的简单的`WSGI server`，一般用于服务器调试，生产环境下建议用其他`WSGI server`。

Web server运行Web application

## 请求传递详解

![WSGI](http://imgbox.com/mrbsG2Ts)

## 示例

```python
def application(environ, start_response):
    status = '200 OK'
    output = 'Hello, world'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-length', str(len(output)))
    ]
    start_response(status, response_headers)
    return [output]
```

```sh
uwsgi --http 0.0.0.0:8000 --wsgi-file userver.py --master --processes 4 --threads 2
```

执行这个命令会产生4个uwsgi进程（每个进程2个线程），1个master进程，当有子进程死掉时再产生子进程，1个 the HTTP router进程，一个6个进程。

这个Http route进程的地位有点类似nginx，(可以认为与nginx同一层)负责路由http请求给worker, Http route进程和worker之间使用的是uwsgi协议