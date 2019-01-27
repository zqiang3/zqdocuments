## 基本数据类型
```c++
    cout << "Bits per byte: " << CHAR_BIT << endl;

    cout << "size of type:" << endl;
    cout << "char is " << sizeof (char) << " bytes." << endl;
    cout << "short is " << sizeof(short) << " bytes." << endl;
    cout << "int is " << sizeof(int) << " bytes." << endl;
    cout << "long is " << sizeof(long) << " bytes." << endl;
    cout << "long long is " << sizeof(long long) << " bytes." << endl;
    cout << "float is " << sizeof(float) << " bytes." << endl;
    cout << "double is " << sizeof(double) << " bytes." << endl;

    cout << endl;
    cout << "maximum values:" << endl;
    cout << "short: " << SHRT_MAX << endl;
    cout << "int: " << INT_MAX << endl;
    cout << "unsigned int: " << UINT_MAX << endl;
    cout << "long: " << LONG_MAX << endl;
    cout << "long long: " << LLONG_MAX << endl;
```

**字符的字面量**
在Release 2.0之后，c++将字符常量存储为char类型，而不是int类型
```c

int main()
{
    char c = 'c';
    printf("sizeof char: %d\n", sizeof(c));
    printf("字符的字面量被存储为int: %d", sizeof('c'));
}

```

**char16_t, char32_t**
```c++
int main()
{
    using namespace std;

    char16_t ch2 = u'q';
    cout << ch2 << endl;
    cout << sizeof ch2 << endl;
}

> g++ -std=c++11 test.cpp
```

