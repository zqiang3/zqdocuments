## 原型

```c
int snprintf(char *restrict buf, size_t n, const char * restrict  format, ...);
```

函数说明:最多从源串中拷贝n－1个字符到目标串中，然后再在后面加一个0。所以如果目标串的大小为n 的话，将不会溢出。

函数返回值:若成功则返回欲写入的字符串长度，若出错则返回负值。