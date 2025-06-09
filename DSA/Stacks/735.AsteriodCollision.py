from list import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        size = len(asteroids)

        for a in asteroids:
            while stack and stack[-1] > 0  and a < 0:
                if abs(stack[-1]) == abs(a):
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(a):
                    break
                else:
                    stack.pop()
                    continue
            else:
                stack.append(a)
        return list(stack)
