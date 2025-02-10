class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        subtree = []

        def helper(i:int ):
            if i == len(digits):
                res.append(''.join(subtree[:]))
                return
            # subtree.append(keyboard[digits[i]])
            for ch in keyboard.get(digits[i]):
                subtree.append(ch)
                helper(i+1)
                subtree.pop()
        helper(0)
        return res






