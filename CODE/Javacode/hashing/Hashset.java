package HASHING;

import java.util.HashSet;
import java.util.Set;

public class Hashset {
    public static void main(String[] args) {
        Set<Integer>  map= new HashSet<>();
        map.add(100);
        map.add(10);
        map.add(100);
        System.out.println(map.size());
        System.out.println(map+" ");

    }
}
