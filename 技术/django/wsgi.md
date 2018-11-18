## wsgi是什么

wsgi is the web server gateway interface.

1. 浏览器发送一个HTTP请求
2. 服务器收到请求，生成响应内容
3. 服务器把响应内容返回给浏览器
4. 浏览器收到响应，展示内容

最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

我们用python专注于生成HTML文档，不希望接触到TCP连接、HTTP原始请求和响应格式。WSGI是一个统一的接口，让我们专心用python写Web业务。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。

```python
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return '<h1>Hello, web!</h1>'
```

上面的`application()`函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

- environ：一个包含所有HTTP请求信息的`dict`对象；
- start_response：一个发送HTTP响应的函数。

有了WSGI，我们关心的就是如何从`environ`这个`dict`对象拿到HTTP请求信息，然后构造HTML，通过`start_response()`发送Header，最后返回Body。

不过，等等，这个`application()`函数怎么调用？如果我们自己调用，两个参数`environ`和`start_response`我们没法提供，返回的`str`也没法发给浏览器。

所以`application()`函数必须由WSGI服务器来调用。



无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过`environ`获得，HTTP响应的输出都可以通过`start_response()`加上函数返回值作为Body。

## 简单示例

```python
# server.py
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print 'Saving HTTP on port 8000'

httpd.serve_forever()
```

```python
# hello.py
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method == 'GET' and path == '/':
        return handle_home(environ, start_response)
    if method == 'POST' and path == 'sign':
        return handle_sign(environ, start_response)
```

## Flask示例

```pyton
# app.py
from flask import Flask
from flask import request 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''
    <form action='/sign' method='post'>
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">sign in</button></p>
    </form>
'''

@app.route('/sign', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>hello, admin</h3>'

    return '<h3>Bad user name or password</h3>'


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
```

