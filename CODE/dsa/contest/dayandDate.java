package CODE;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class dayandDate {
    public static void main(String[] args) {
        LocalDate today=LocalDate.now();
        LocalDateTime dateTime=LocalDateTime.now();
        System.out.println(today.getDayOfWeek());
        while (true){
            LocalTime time=LocalTime.now();
            System.out.print("\033[H\033[J");
            System.out.println(time.format(java.time.format.DateTimeFormatter.ofPattern("HH:mm:ss")));
            try {
                Thread.sleep(1000);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }



    }
}
