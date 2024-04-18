package CP.CODECHEF;

import java.lang.ref.SoftReference;

public class lexigraph {
    public static void main(String[] args) {
        String s="welcometojava";
        char[] arr=s.toCharArray();
        int k=3;
        String smallest = s.substring(0,k);
        String largest =s.substring(0,k);

        for(int i=0;i<=s.length()-k;i++){
            String sub=s.substring(i,i+k);
            if(sub.compareTo(smallest)<0){
                smallest=sub;
            }
            if(sub.compareTo(largest)>0){
                largest=sub;
            }
        }
        System.out.println(smallest);
        System.out.println(largest);

//        for(int i=1;i<arr.length;i++){
//            if(max.c)
//        }
    }
}
