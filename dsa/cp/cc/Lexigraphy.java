package CP.CODECHEF;

import java.awt.image.AreaAveragingScaleFilter;
import java.util.Arrays;
import java.util.Collections;

public class Lexigraphy {
    public static void main(String[] args) {

//        Scanner sc=new Scanner(System.in);
        String A="hello";
        String B="java";
        /* Enter your code here. Print output to STDOUT. */
        int size=A.length()+B.length();
        System.out.println(size);
        char[] arr=A.toCharArray();
//        Arrays.sort(arr);
        char[] arr2=B.toCharArray();
//        Arrays.sort(arr2);
        String compare=A.compareTo(B)>0?"Yes":"No";
        System.out.println(compare);
        String one=Character.toUpperCase(A.charAt(0))+A.substring(1);
        String two=Character.toUpperCase(B.charAt(0))+B.substring(1);
        System.out.println(one+" "+two);
//        System.out.println(arr2);
//        System.out.println(arr);
//        for(int i=0;i<arr.length;i++){
//            for(int j=0;j<=i;i++){
//                if(arr[i]>arr[j]){
//                    System.out.println("No");
//                    break;
//                }
//            }
//        }

    }
}
