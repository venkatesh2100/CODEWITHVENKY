package CP.CODECHEF;

import java.util.Scanner;

public class OldsaintHero {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        int t=sc.nextInt();
           int len1=0,len2=0;
        while (t-->0){
            int arr2[]=new int[3];
            int arr[]=new int[3];
            for(int i=0;i<3;i++) {
                arr[i] = sc.nextInt();
            }
            for(int num:arr) {
                if (num == 0) {
                    len1++;
                }
            }
                for(int j=0;j<3;j++) {
                    arr2[j] = sc.nextInt();
                }
                for(int sums:arr2) {
                    if (sums == 0) {
                        len2++;
                    }
                }
                    if(len1==len2) System.out.println("pass");
                    else System.out.println("fail");
            }
        }
    }
