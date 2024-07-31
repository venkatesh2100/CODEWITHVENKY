
// package ARRAYS;
import java.util.*;

public class ArrayCopy {
    public static void main(String[] args) {
        ArrayList<Integer> l = new ArrayList<>();
        l.add(1000);
        l.add(100000);
        l.add(100);
        l.add(1000);
        l.add(10000000);
        l.trimToSize();
        for (int i = 0; i < l.size() - 1; i++) {
            int min = i;
            for (int j = i + 1; j < l.size(); j++) {
                if (l.get(min) > l.get(j)) {
                    min = j;
                }
            }
            int temp = l.get(i);
            l.set(i, l.get(min));
            l.set(min, temp);
        }
        System.out.println(l);
        // Collections.sort(l);
        System.out.println(l);
        System.out.println(l.hashCode());
        System.out.println(l.size());
        String[][] arr = {
                { "Affogato", "Americano", "Cappuccino", "Corretto", "Cortado", "Doppio", "Espresso" },
                { "Frappucino", "Freddo", "Lungo", "Macchiato", "Marocchino", "Ristretto" }
        };

        String[] copy = new String[5];
        String[] name = new String[2];
        System.out.println(name[0]);
        System.out.println(Arrays.toString(copy));
        System.out.println(Arrays.stream(copy).count());
        if (copy.length == Arrays.stream(copy).count()) {
            System.out.println("true");
        }
        // System.arraycopy(arr,4,copy,1,3);
        // for(String coffe:copy){
        // System.out.println(coffe+" ");
        // }
        System.out.println(Arrays.toString(copy));
        // for(String elements:arr){
        // System.out.print(elements+" ");
        // }
        // System.out.println(Arrays.toString(arr));
        // System.out.println(Arrays.binarySearch(arr, "Lungo"));
        System.out.println(Arrays.deepToString(arr));
        // System.out.println(Arrays.binarySearch(copy,"Doppio"));
    }

}
