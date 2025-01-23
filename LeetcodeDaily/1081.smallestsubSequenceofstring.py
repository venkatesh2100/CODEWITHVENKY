from collections import Counter
class Solution:

    def smallestSubsequence(self, s: str) -> str:

        dic=Counter(s)
        nagesh=set()
        st=[]

        for i in s:
            if i not in nagesh:
                while st and st[-1]>i and dic[st[-1]]>0:
                    nagesh.discard(st.pop())
                st.append(i)
                nagesh.add(i)
            dic[st[-1]]-=1
        return ''.join(st)
