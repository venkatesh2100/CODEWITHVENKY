package CP.CODECHEF;

public class PrimesNumInrange {
    public static void main(String[] args) {
        System.out.println(solve(0, 10)); // Output: 5
    }

    public static int solve(int start, int end) {
        int count = 0;
        for (int m = 0;m<11 ; m++) {
            int powerOf3 = (int) Math.pow(3, m);
            if (powerOf3 > end) break;
            for (int n = 0;n<11 ; n++) {
                int prime = powerOf3 * (int) Math.pow(2, n) + 1;
                if (prime >= start && prime < end) {
                    if(prime%2!=0&&prime%3!=0){
                            count++;
                    }
                } else if (prime >= end) {
                    break;
                }
            }
        }
        return count;
    }
}

