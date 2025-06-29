class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        N = len(grid)
        cf = 0
        for i in range(N):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    cf += 1
        # Fresh oranges and Rottten Oranges.
        if cf == 0:
            return 0
        if not q:
            return - 1
        min = -1
        dic = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q:
            # print(q)
            for i in range(len(q)):
                i, j = q.popleft()
                # print('i and j',i,j)
                for x in dic:
                    newi = i + x[0]
                    newj = j + x[1]
                    # on bound
                    if 0 <= newi < N and 0 <= newj < N and grid[newi][newj] == 1:

                        # print('newv :',newi,newj)
                        cf -= 1
                        grid[newi][newj] = 2
                        q.append([newi, newj])
            min += 1
        if cf == 0:
            return min
        return -1
