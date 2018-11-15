## 读取字符
```
c
#include <stdio.h>

int main()
{
    printf("input a char\n");
    char c;
    // scanf("%c", &c);
    scanf(" %c", &c);
    printf ("the char you inpus is %c\n", c);
    printf ("the char you inpus is %#x\n", c);


    return 0;
}
```
