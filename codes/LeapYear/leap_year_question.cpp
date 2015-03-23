#include <iostream>
using namespace std;

int is_leap_year(int year)
{
    if(year % 400 ==0)
        return 1;
    else if(year % 4 == 0 && year % 100 != 0)
        return 1;
    else
        return 0;
}

int main()
{
    int year = 2000;
    cout << is_leap_year(year) << endl;
}
