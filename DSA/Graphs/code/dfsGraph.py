
def dfs(graph, start, res, vis):
    if not graph:
        return None
    vis.add(start)
    res.append(start)
    for nei in graph[start]:
        if nei not in vis:
            dfs(graph, nei, res, vis)
    return res


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['A']
}


res = []
vis = set()
# print(dfs(graph, 'A', res, vis))

print(dfs(graph, 'B', res, vis))
