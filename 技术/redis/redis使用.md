## 启动、停止、重启

```bash
/etc/init.d/redis-server stop
/etc/init.d/redis-server start
/etc/init.d/redis-server restart
redis-cli shutdown
kill -9 PID

```

## 查看端口

```bash
netstat -lntp | grep 6379
```

gzzhangqiang2014

jia@1993