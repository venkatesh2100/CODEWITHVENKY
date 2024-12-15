import java.util.Arrays;

//Input: points = [[10,16],[2,8],[1,6],[7,12]]
//Output: 2
//Explanation: The balloons can be burst by 2 arrows:
//- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
//- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points,(a,b))->Integer.compare(a[1],b[1]));
        int arrow=1;
        int lastElement=points[0][1];
        for(int i=1;i< points.length;i++){
            if(points[i][0]>lastElement){
                arrow++;
                lastElement=points[i][1];
            }
        }
        return arrow;




    }
}