class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        res = [0] * n

        left = 0
        operations = 0
        for i in range(n):
            res[i] += operations
            if boxes[i] == "1":
                left +=1
            operations += left
            print(res)

        right = 0
        operations = 0
        for i in range(n-1,-1,-1):
            res[i] += operations
            if boxes[i] == '1':
                right +=1
            operations +=right
            print(res)


        return res
