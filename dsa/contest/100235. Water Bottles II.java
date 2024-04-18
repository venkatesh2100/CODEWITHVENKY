package CODE;

class Solution {

    public static void main(String[] args) {
        System.out.println(maxBottlesDrunk(10,3));
    }
    public static int maxBottlesDrunk(int numBottles, int numExchange) {
        //init
        int Bottle_drunk=0;
        int Empty_Bottle=0;
        while(numBottles>0){
            int temp=numBottles;
            Bottle_drunk+=temp;
            Empty_Bottle+=temp;
            numBottles=0;
            while (Empty_Bottle>=numExchange){
                Empty_Bottle-=numExchange;
                numExchange++;
                numBottles++;
            }

        }
        return Bottle_drunk;
    }
}