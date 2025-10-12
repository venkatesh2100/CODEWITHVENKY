class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        def Check(num):
            for i in range(len(baskets)):
                if num <= baskets[i]:
                    baskets[i] = 0
                    return True
            return False

        res = 0
        for num in fruits:
            if not Check(num):
                res += 1

        return res
