package CP.CODECHEF;

import java.sql.SQLOutput;

public class Multiple5 {
    public static void main(String[] args) {
        int n=133;
        int size=3;
        boolean flag=false;
        String num=Integer.toString(n);
        for(int i=0;i<size;i++){
            if (num.charAt(i) == '5' || num.charAt(i)=='0') {
                flag = true;
                break;
            }
        }
        if(flag==true){
            System.out.println("YES");
        }else System.out.println("NO");
//        char[] arr=num.toCharArray();
//        for(int i=0;i<size;i++){
//            if(arr[i] == 5){
//                System.out.println("YES");
//                break;
//            } else if (arr[i]==0) {
//                System.out.println("NO");
//                break;
//            } else{
//                System.out.println("NO");
//            }
//        }
    }
}
