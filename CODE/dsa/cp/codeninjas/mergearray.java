package CP.CODENINJAS;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class mergearray {
   public static List< Integer > sortedArray(int []a, int []b) {
        // Write your code here
        ArrayList<Integer> ll=new ArrayList<>();
        for(int nums:a){
          if(!ll.contains(nums)){
            ll.add(nums);
          }
        }
        for(int nums:b){
          if(!ll.contains(nums)){
            ll.add(nums);
          }
        }
        Collections.sort(ll);
        return ll;
    }
  
}
