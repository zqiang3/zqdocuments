#include <stdio.h>

int is_leap_year(int year)
{
    if(year % 400 == 0)
        return 1;
    else if(year % 4 == 0 && year % 100 != 0)
        return 1;
    else
        return 0;
}

int main()
{
    int year = 2100;
    int result = is_leap_year(year);
    printf("result is: %d", result);
    return 0;

}
