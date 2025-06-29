from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def can_detonate(i, j):
            x1, y1, r1 = bombs[i]
            x2, y2, _ = bombs[j]
            dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
            return dist_sq <= r1 ** 2  # distance squared <= radius squared

        def dfs(i, visited):
            visited[i] = True
            count = 1  # count this bomb
            for j in range(len(bombs)):
                if not visited[j] and can_detonate(i, j):
                    count += dfs(j, visited)
            return count

        max_count = 0
        for i in range(len(bombs)):
            visited = [False] * len(bombs)
            max_count = max(max_count, dfs(i, visited))

        return max_count
