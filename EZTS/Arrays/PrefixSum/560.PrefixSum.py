
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # TODO: Use Presum Logic USING HASHmap

        dic = {0: 1}
        count = 0
        sumi = 0
        for num in nums:
            sumi += num
            # HACK: Prefix sum Logic if sumi - k is in HashMap then ++count
            if sumi-k in dic:
                count += dic[sumi-k]
            dic[sumi] = dic.get(sumi, 0) + 1
        return count
