# Input: piles = [2,4,1,2,7,8]
# Output: 9
# Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
# Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
# The maximum number of coins which you can have are: 7 + 2 = 9.
# On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal

from collections import deque
from enum import pickle_by_enum_name
from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
    #TODO: Top 2 max and then small one 

        que = deque(sorted(piles))

        res = 0 
        print(que)
        while que:
            que.pop()
            que.popleft()
            res+= que.pop()
        return res




arr =  [2,4,1,2,7,8]
sol = Solution()
print( sol.maxCoins(arr))
