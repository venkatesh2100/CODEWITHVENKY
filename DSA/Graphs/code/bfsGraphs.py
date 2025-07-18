from collections import deque

# TODO: Bfs travers the AJ and Store in a Arr


def bfs(graph, start):
    if not graph:
        return None
    visited = set()
    # Que stores the relative elements in the que.
    que = deque([start])
    res = []
    while que:
        node = que.popleft()
        if node not in visited:
            visited.add(node)
            res.append(node)

            for nei in graph[node]:
                if nei not in visited:
                    que.append(nei)
    return res


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['A']
}

print(bfs(graph, 'A'))
print(bfs(graph, 'B'))
