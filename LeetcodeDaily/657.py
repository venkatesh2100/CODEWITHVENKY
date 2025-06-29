from typing import List


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for m in moves:
            if m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
            elif m == 'R':
                x += 1
            elif m == 'L':
                x -= 1
        return True if x == 0 and y == 0 else False
