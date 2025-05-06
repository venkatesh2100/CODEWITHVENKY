class Solution:
    def Subarr(self, arr):
        print(arr)
        for left in range(len(arr)):
            for right in range(left, len(arr)):
                for i in range(left, right + 1):
                    print(arr[i], end=" ")
                print()  # for a new line after each subarray

# Example usage
sol = Solution()
sol.Subarr([1, 2, 3])
