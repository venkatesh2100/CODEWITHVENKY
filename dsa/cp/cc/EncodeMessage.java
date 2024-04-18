package CP.CODECHEF;

import java.util.Scanner;

public class EncodeMessage {
    public static void main(String[] args) {
        Message();
    }
    static  void Message(){
        Scanner sc =new Scanner(System.in);
        int t=sc.nextInt();
        while (t-->0){
            int  size=sc.nextInt();
            sc.nextLine();
            String name=sc.nextLine();
            char[] arr=name.toCharArray();
            for(int i=0;i<size-1;i+= 2){//For reverse the index of the String
                    char temp=arr[i+1];
                    arr[i+1]=arr[i];
                    arr[i]=temp;
            }
            for(int i=0;i<size;i++){
                arr[i]=(char)(25- (int)(arr[i])+2*97);
            }
            System.out.println(new String(arr));
        }
    }
}
