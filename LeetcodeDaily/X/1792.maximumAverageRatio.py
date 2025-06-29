import heapq
class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        ##! using Max heap
        ##? This function calculates the Gains
        total=0
        def calculateGain(passes:int,students:int)->float:
            return passes+1/students+1 - passes/students

        maxheap=[]
        ##? intialize and push the gai passes and students to the Maxheap
        for passes,students in classes:
            gain=calculateGain(passes,students)
            heapq.heappush(maxheap,(-gain,passes,students))

        ##? Now we distrubuting the Extra Students to the maximum gain worthy Classes using Maxheap
        for i in range(extraStudents):
            gain,passes,students=heapq.heappop(maxheap)
            heapq.heappush(maxheap,(-calculateGain(passes+1,students+1),passes+1,students+1))

        while maxheap:
          gain,passes,students=heapq.heappop(maxheap)
          total+=passes/students


        return total/len(classes)
A=Solution()
call=A.maxAverageRatio([[1,2],[3,5],[2,2]],2)
print(call)
