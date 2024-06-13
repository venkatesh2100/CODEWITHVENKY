package HASHING;

public class FindtheMissing {

    public static void main(String[] args) {
        int[] arr={1,2,4,5,6};
        FindtheMissing ob1=new FindtheMissing();
        System.out.println(ob1.firstMissingPositive(arr));
    }

        public int firstMissingPositive(int[] nums) {
            int n = nums.length;
            boolean[] found = new boolean[n+1];
            for(int i = 0;i< n; i++){
                if (nums[i]>0 && nums[i]<= n){
                    found[nums[i]]=true;

                }
            }
            for(int i= 1;i<=n;i++){
                if(!found[i]){
                    return i;
                }
            }
            return n+1;
        }
}
