class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        #Use a hashmap to Count the Frequiencies of Products

        hashmap = {}
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i] * nums[j]
                hashmap[product] = hashmap.get(product ,0) + 1
        # print(hashmap.values())
        for val in hashmap.values():
            # if val == 4:
            #     count +=8
            if val >=2:
                # sub = val - 4
                count += (val * (val-1))//2 * 8
        return count 
