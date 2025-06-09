
from collections import deque
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        
        #TODO: Visited Graph Finding a Loop or circle
        N = len(favorite)
        visited = [False] * N
        long2cycle = []
        longest_cycle = 0
        for i in range(N):
            if visited[i]:
                continue
            start= i
            curr = i
            curr_set = set()
            while not visited[curr]:
                visited[curr] = True
                curr_set.add(curr)
                curr = favorite[curr]
            # print(curr_set)
            # print(curr)

            if curr in curr_set:
                cyclelen = len(curr_set)

                while start!=curr:
                    cyclelen -=1
                    start = favorite[start]
                longest_cycle = max(cyclelen,longest_cycle)
                # print(longest_cycle)
                if cyclelen == 2:
                    long2cycle.append([curr,favorite[curr]])
        
        #HACK: Now constructor AdjList
        AdjList = [[] for _ in range(N)]
        for idx ,val in enumerate(favorite):
            AdjList[val].append(idx)
        print(AdjList)
        
        def bfs(src ,dst):
            q =deque([(src ,0)])
            # print(q)
            maxlen = 0
            while q:
                # print(q ,src ,dst)
                src ,length  = q.popleft()
                if src == dst:
                    continue
                maxlen = max(maxlen , length)
                for nei in AdjList[src]:
                    # print(q)
                    q.append((nei ,length+1))
            return maxlen
            
        chain_sum =  0 
        for n1 ,n2 in long2cycle:
            chain_sum += bfs(n1,n2) + bfs(n2,n1) + 2 
        return max(longest_cycle ,chain_sum)
