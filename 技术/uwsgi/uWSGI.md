## uWSGI的安装
pip install uwsgi

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