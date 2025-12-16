class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        new_s = ''

        for w in s:
            if w.isalnum():
                new_s+= w.lower()

        print(new_s)

        return  self.palindrome(new_s) 


    def palindrome(self, s):
        
        l = 0
        r = len(s) -1 

        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True 
    
