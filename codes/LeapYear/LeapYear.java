
public class LeapYear
{

    public static Boolean is_leap_year(Integer year)
    {
        if(year % 400 == 0)
            return true;
        else if(year % 4 == 0 && year % 100 != 0)
            return true;
        else
            return false;
    }

    public static void main(String[] args)
    {
        Integer year = 2100;
        System.out.println(LeapYear.is_leap_year(year));
    }
}
