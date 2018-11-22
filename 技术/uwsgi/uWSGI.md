## uWSGI的安装

uWSGI is a (big) C application, so you need a C compiler (like gcc or clang) and the Python development headers.

```bash
pip install uwsgi
# 或出错可能是缺少python-dev build-essential
sudo apt-get install python-dev
sudo apt-get install build-essential  # On a Debian-based distro
```



## uWSGI的主要特点
超快的性能
低内存占用，实测为apache2的mod_wsgi的一半左右
多app管理
详尽的日志功能，可以用来分析app性能和瓶颈
高度可定制，内存大小限制，服务一定次数后重启等

## quick start

uwsgi --http :9090 --wsgi-file foobar.py
--processes
--threads

monitor understanding what is going on is vital in production deployment

--chdir  move to a specific directory

## 在前端放置nginx

Do not use `--http` when you have a frontend webserver or you are doing some form of benchmark, use `--http-socket`. Continue reading the quickstart to understand why.

### 使用uwsgi协议

nginx按如下方式配置：

```nginx
location / {
    uwsgi_pass 127.0.0.1:9090;
}
```

This means “pass every request to the server bound to port 9090 speaking the uwsgi protocol”.

nginx 会将每个请求转发到本地9090端口，使用的是uwsgi协议。

运行usgi：(注意使用 --socket)

```bash
uwsgi  --socket 127.0.0.1:9090 --wsgi-file testapp.py
```

## 使用http协议

nginx配置

```nginx
location / {
    proxy_pass http://127.0.0.1:9090;
}
```

运行usgi：(注意使用 --http-socket，不同于--http, --http是直接启一个http代理接收请求)

```bash
uwsgi  --socket 127.0.0.1:9090 --wsgi-file testapp.py
```

uwsgi_pass使用的是uwsgi协议，proxy_pass使用HTTP协议与uWSGI server交互。

## nginx和uwsgi的关系

nginx是前端服务器，负责接收请求。

uwsgi是一种通信协议，负责在服务器和应用程序间进行数据通信。

**通信过程**： 

客户端发送一个http请求，被nginx服务器接收，nginx服务器将请求转发给uwsgi,uwsgi将请求转发给实现uwsgi协议的应用程序(flask,gunicorn等等)