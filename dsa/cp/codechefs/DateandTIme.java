package CP.CODECHEF;

import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Locale;

public class DateandTIme {
    public static void main(String[] args) {
        System.out.println(findDay(8,14,2017));

    }
    public static String findDay(int month, int day, int year) {

        Calendar cal=Calendar.getInstance();
        cal.set(year,month-1,day);
        int dayofweek=cal.get(Calendar.DAY_OF_WEEK);
        String[] arr = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        String day1=arr[dayofweek];
        return day1;
    }
}
