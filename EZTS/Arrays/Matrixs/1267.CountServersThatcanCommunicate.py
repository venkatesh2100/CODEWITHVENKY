from collections import deque


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        # store = set()
        que = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    # store.add(r)
                    # store.add(c)
                    que.append([r, c])
        # HACK: NEW Brute Force
        count = 0
        # print(que)
        # print(store)

        while que:
            r, c = que.popleft()
            connect = False
            for nr in range(col):
                if grid[r][nr] == 1 and nr != c:
                    connect = True
                    # print(r, nr)
                    break
            for nc in range(row):
                if grid[nc][c] == 1 and nc != r:
                    connect = True
                    break
            if connect:
                count += 1

        return count

        # HACK: Brand new appraoch get the String 024 and check the que
        while que:
            r, c = que.popleft()
            if r or c in store:
                count += 1
        return count

        # TODO: check whether +one row or col has 1 or not
        # oneplus = [[0,1] , [1,0] ,[-1, 0], [0,-1]]
        while que:
            r, c = que.popleft()
            for onerow, onecol in oneplus:
                nr, nc = onerow + r, onecol + c
                if 0 <= nr < row and 0 <= nc < col:
                    if grid[nr][nc] == 1:
                        count += 1
                        break
        return count
