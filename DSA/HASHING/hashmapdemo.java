package HASHING;

import java.util.HashMap;

public class hashmapdemo {
    public static void main(String[] args) {
        HashMap<String,Integer> map=new HashMap<>();
        map.put("venky",2005);
        System.out.println(map);
        map.put("saiKumar",2004);
        System.out.println(map.size());
    }
}
