
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {i: [] for i in range(numCourses)}
        # print(adjList)
        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
        # print(adjList)
        result = []
        for query in queries:
            visited = [False] * numCourses
            result.append(self.isPre(adjList, visited, query[0], query[1]))
        return result

    def isPre(self, adjList: dict, visited: List[bool], curr: int, target: int):
        visited[curr] = True

        if curr == target:
            return True
        for adj in adjList.get(curr):
            if not visited[adj]:
                if self.isPre(adjList, visited, adj, target):
                    return True
        # print("Case 1")
        return False
