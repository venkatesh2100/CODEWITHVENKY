package HASHING;

import java.util.HashMap;

public class RomamToInt {
    public static void main(String[] args) {
        String s="MCMXCIV";
        System.out.println(Roman(s));
    }
    public  static int Roman(String s){
        int ans=0;
        HashMap<Character ,Integer> map=new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        char[] arr=s.toCharArray();
//        if(arr[0]=='I'&&arr[1]=='V'||arr[1]=='X'||arr[1]=='L'||arr[1]=='C'||arr[1]=='D'||arr[1]=='M'){
//            ans=map.get(arr[1])-map.get(arr[0]);
//            return ans;
//        }
        for(int i=0;i<arr.length;i++){
            if(i<arr.length-1&&map.get(arr[i])<map.get(arr[i+1])){
                ans-=map.get(arr[i]);
            }else{
                ans+=map.get(arr[i]);
            }
        }

        return ans;
    }
}
