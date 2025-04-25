class Solution {
public:
    int minBitFlips(int start, int goal) {
        //Mini BitstoFlip 
        int res = start ^ goal;
        int c;
        while(res){
            if(res  & 1){
            ++c;
            }
            res = res >> 1;
        }
        return c;
        
    }
};
