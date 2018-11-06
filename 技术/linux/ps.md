## 查看进程的运行时间

```bash
ps -eo pid,tty,user,comm,lstart,etime | grep 17674
```

**参数说明**：

pid：进程ID

tty：终端

user：用户

comm：进程名

lstart：开始时间

etime：运行时间