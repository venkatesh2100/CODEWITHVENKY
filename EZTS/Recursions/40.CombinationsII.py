class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #TODO: Use RT to Figure out the Code and then Try to Eliminate the Duplicates use memo or sort.        
        res = []
        subset = []
        candidates.sort()
        # memo = []
        def dfs(i:int ,curr_sum:int):
            if curr_sum > target:
                return
            if curr_sum == target:
                # sort_values = sorted(subset[:])
                # if sort_values not in memo:
                    # res.append(sort_values)
                # memo.append(sort_values)
                res.append(subset[:])
                return
            if i >= len(candidates):
                return 
            
            subset.append(candidates[i])
            dfs(i+1,curr_sum + candidates[i])

            subset.pop()
            while i+1 < len(candidates)  and candidates[i] ==candidates[i+1]:
                i+=1
            dfs(i+1,curr_sum)
        dfs(0,0)
        print(dfs(0,0))
        return res
