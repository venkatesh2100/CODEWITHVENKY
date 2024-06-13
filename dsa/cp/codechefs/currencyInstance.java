package CP.CODECHEF;
import  java.util.Scanner;
import java.text.NumberFormat;
import java.util.*;
public class currencyInstance {
    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
        double payment = 12324.123;

        // Write your code here.
        NumberFormat usFormat= NumberFormat.getCurrencyInstance(Locale.US);
        String us=usFormat.format(payment);

        NumberFormat  inFormat=NumberFormat.getCurrencyInstance(new Locale("en","IN"));
        String india=inFormat.format(payment);
        NumberFormat chFormat=NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china=chFormat.format(payment);
        NumberFormat fraFormat=NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france=fraFormat.format(payment);
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
