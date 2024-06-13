// package ARRAYS;

import javax.rmi.ssl.SslRMIClientSocketFactory;
import java.util.Scanner;

public class BTwoDimensional {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
//        System.out.println("Enter the size of Array ROW and COL:");
//        int row=sc.nextInt();
//        int col=sc.nextInt();
        int[][] arr=new int[2][2];
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[i].length;j++){
                arr[i][j]= sc.nextInt();
            }
        }
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[i].length;j++){
                System.out.print(arr[i][j]*2+" ");
            }
        }
    }
}
