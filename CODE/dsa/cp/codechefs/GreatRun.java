package CP.CODECHEF;

import java.util.Scanner;

public class GreatRun {
    public static void main(String[] args) {
        maxGirl();
    }
        public static void maxGirl(){
         Scanner sc = new Scanner(System.in);
         int t = sc.nextInt();
            while (t-->0){
                int N= sc.nextInt();
                int K=sc.nextInt();
                int[] arr=new int[N];
                for(int i=0;i<N;i++){
                    arr[i]=sc.nextInt();
                }
                int sum=0,max=0;
                for(int i=0;i<N-K;i++){
                    for(int j=i;j<i+K;j++){
                        sum+=arr[j];
                    }
                    if(max<sum){
                        max=sum;
                    }
                    sum=0;
                }
                System.out.println(max);
            }
        }

        //        while(t-->0){
//            int N=sc.nextInt();//Total path
//            int K=sc.nextInt();//Max speed distance
//            int[] arr=new int[N];
//            int max1=0,max2=0;
//            for(int i=0;i<N;i++){
//                arr[i]=sc.nextInt();
//                if(arr[i]>max1){
//                    max1=arr[i];
//                }
//            }
//            for(int num:arr){
//                if(num>max2&&num!=max1){
//                    max2=num;
//                }
//            }
//            System.out.println(max1+max2);
//        }

}
