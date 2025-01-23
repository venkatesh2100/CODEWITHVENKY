package ARRAYS;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class ArrayListele<S> {
   public static void main(String[] args) {
       ArrayList<String> cars=new ArrayList<String>();
       ArrayList<Integer> values=new ArrayList<Integer>();
       values.add(75);
       values.add(25);
       cars.add("Ferrari");
       cars.add("Lambo");
       Collections.sort(cars);
       Collections.sort(values);
       for(int j:values){
           System.out.println(j);
       }
       System.out.println(cars.size());
       for(String i:cars){
           System.out.println(i);
       }
       System.out.println("Hell");
  }
}
