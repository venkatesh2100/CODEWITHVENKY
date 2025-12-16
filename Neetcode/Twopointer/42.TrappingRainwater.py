class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        l = 0 
        r = n - 1
        leftMax = height[0]
        rightMax = height[r]
        water = 0 
        while l < r:

            if leftMax < rightMax:

                l+=1
                leftMax = max(leftMax,height[l])
                water+= leftMax - height[l]

            else:
                
                r-=1
                rightMax = max(rightMax , height[r])
                water+= rightMax - height[r]

        return water

