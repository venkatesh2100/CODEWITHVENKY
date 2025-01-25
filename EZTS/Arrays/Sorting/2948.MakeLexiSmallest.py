from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int):
        numsCopy: List[int] = sorted(nums)
        # TODO: Create Group using HashMaps

        currGroupNum = 0
        groupNum = {}
        groupNum[numsCopy[0]] = currGroupNum

        groupList = {}
        groupList[currGroupNum] = deque([numsCopy[0]])

        for i in range(1, len(nums)-1):
            if abs(numsCopy[i] - numsCopy[i-1]) > limit:
                currGroupNum += 1

            groupNum[numsCopy[i]] = currGroupNum
            if currGroupNum not in groupList:
                groupList[currGroupNum] = deque([])

            groupList[currGroupNum].append(numsCopy[i])
        # TODO: Now generate the Arr with groupList
        for i in range(len(nums)):
            val = nums[i]
            group = groupNum[val]
            nums[i] = groupList[group].popleft()
        return nums


ans = Solution()
limit = 3
nums = [1, 7, 6, 18, 2, 1]
print(ans.lexicographicallySmallestArray(nums, limit))

# currGroup = 0
# numToGroup = {}
# numToGroup[numsCopy[0]] = currGroup
#
# # Step 3: Map each number in the sorted array to a group
# groupToList = {}
# groupToList[currGroup] = deque([numsCopy[0]])
#
# # Step 4: Group numbers based on the limit difference
# for i in range(1, len(numsCopy)):
#     if abs(numsCopy[i] - numsCopy[i - 1]) > limit:
#         currGroup += 1
#     numToGroup[numsCopy[i]] = currGroup
#     if currGroup not in groupToList:
#         groupToList[currGroup] = deque()
#     groupToList[currGroup].append(numsCopy[i])
#
# # Step 5: Rebuild the original array by filling from the sorted groups
# for i in range(len(nums)):
#     num = nums[i]
#     group = numToGroup[num]
#     nums[i] = groupToList[group].popleft()
#
# return nums

# TODO HACK:This Approach is Fucked Up: Iterate the Loop until Limit Possible difference.

# for i in range(len(nums)):
#     idx = i
#     mini = nums[i]
#     for j in range(i+1 , len(nums)):
#         val = nums[i] - nums[j]
#         if val > 0 and val <= limit:
#             # nums[i] , nums[j] = nums[j]  , nums[i]
#             if nums[j] < mini:
#                 mini = nums[j]
#             # print(mini)
#                 idx = j
#             # print(f'J value:' ,idx)
#         # print(nums)
#     # print(i ,idx)
#     if idx!=i:0
#         nums[i] , nums[idx] = nums[idx]  , nums[i]

# return nums

# n = len(nums)

# # Step 1: Build graph based on the swap condition
# graph = defaultdict(list)
# for i in range(n):
#     for j in range(i + 1, n):
#         if abs(nums[i] - nums[j]) <= limit:
#             graph[i].append(j)
#             graph[j].append(i)

# # Step 2: Find all connected components using DFS
# visited = [False] * n
# def dfs(node, component):
#     visited[node] = True
#     component.append(node)
#     for neighbor in graph[node]:
#         if not visited[neighbor]:
#             dfs(neighbor, component)

# # Step 3: Process each connected component
# for i in range(n):
#     if not visited[i]:
#         component = []
#         dfs(i, component)
#         # Sort the indices in the component based on the values of nums
#         component_values = sorted([nums[idx] for idx in component])
#         # Place the sorted values back into their respective positions
#         for idx, value in zip(sorted(component), component_values):
#             nums[idx] = value

# return nums
