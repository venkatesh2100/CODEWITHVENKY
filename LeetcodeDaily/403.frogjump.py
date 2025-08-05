class Solution:
    def canCross(self, stones: List[int]) -> bool:
        "using bavck tracking Approch we can Do it"
        step_dicrection = [1, 0, -1]

        def backtrack(stones, index):

            for i step_dicre
