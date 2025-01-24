# 🔫 Graph Data Structure in Python and Java

## 1. 🔄 Basics of Graphs

A **graph** is a collection of nodes (called vertices) and edges connecting them. It can be:

- **Directed**: ➡️ Edges have direction.
- **Undirected**: ⬆️🔼 Edges do not have direction.
- **Weighted**: ⚖️ Edges have weights.
- **Unweighted**: ❌ Edges do not have weights.

### Representation:

1. **Adjacency List**: 🔄 Most commonly used, represented as a dictionary or list of lists.
2. **Adjacency Matrix**: 🔢 A 2D array where `matrix[i][j]` represents the edge between vertex `i` and vertex `j`.

---

## 2. 🔧 Graph Syntax and Implementation

### Python Implementation

#### Adjacency List:

```python
# Using a dictionary for adjacency list
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: []
}
```

#### Adjacency Matrix:

```python
# Adjacency Matrix
n = 4  # Number of vertices
graph = [[0] * n for _ in range(n)]
graph[0][1] = 1
```

#### Adding Edges:

```python
from collections import defaultdict

graph = defaultdict(list)
graph[0].append(1)
graph[0].append(2)
graph[1].append(2)
```

### Java Implementation

#### Adjacency List:

```java
import java.util.*;

class Graph {
    private Map<Integer, List<Integer>> adjList;

    public Graph() {
        adjList = new HashMap<>();
    }

    public void addEdge(int u, int v) {
        adjList.putIfAbsent(u, new ArrayList<>());
        adjList.get(u).add(v);
    }
}
```

#### Adjacency Matrix:

```java
int n = 4; // Number of vertices
int[][] graph = new int[n][n];
graph[0][1] = 1;
graph[1][2] = 1;
```

---

## 3. 🕸️ Graph Traversal Algorithms

### 🚀 Breadth-First Search (BFS)

BFS explores neighbors level by level and is implemented using a queue.

#### Python:

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            queue.extend(graph[node])
```

#### Java:

```java
import java.util.*;

void bfs(Map<Integer, List<Integer>> graph, int start) {
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();
    queue.add(start);

    while (!queue.isEmpty()) {
        int node = queue.poll();
        if (!visited.contains(node)) {
            visited.add(node);
            System.out.print(node + " ");
            queue.addAll(graph.getOrDefault(node, new ArrayList<>()));
        }
    }
}
```

### ⬇️ Depth-First Search (DFS)

DFS explores as far as possible before backtracking. It is implemented using recursion or a stack.

#### Python:

```python
def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

visited = set()
dfs(graph, 0, visited)
```

#### Java:

```java
void dfs(Map<Integer, List<Integer>> graph, int node, Set<Integer> visited) {
    if (!visited.contains(node)) {
        visited.add(node);
        System.out.print(node + " ");
        for (int neighbor : graph.getOrDefault(node, new ArrayList<>())) {
            dfs(graph, neighbor, visited);
        }
    }
}
```

---

## 4. ❓ BFS vs. DFS: How to Choose?

| **Scenario**                            | **Algorithm** |
| --------------------------------------- | ------------- |
| Find shortest path (unweighted graph)   | BFS           |
| Check if a path exists                  | Either        |
| Topological sorting                     | DFS           |
| Detect cycles in directed graphs        | DFS           |
| Search in large graphs with fewer edges | DFS           |
| Search level by level                   | BFS           |

---

## 5. 🎓 Tips for LeetCode Graph Problems

### 🧠 Key Intuitions:

1. **Start with Examples:** Always draw a small example graph to understand the problem visually.
2. **Type of Graph:** Understand whether the graph is directed/undirected, weighted/unweighted.
3. **Traversal vs. Structure:**
   - Use **BFS** when finding shortest paths in unweighted graphs.
   - Use **DFS** for problems like connected components or topological sorting.
4. **Constraints Guide Strategy:**
   - Small graph size (e.g., `n < 1000`): You can afford recursive DFS or adjacency matrix.
   - Large sparse graph: Use adjacency list and iterative BFS/DFS.

### ⏱️ Time Complexity:

| **Operation**        | **Adjacency List** | **Adjacency Matrix** |
| -------------------- | ------------------ | -------------------- |
| Add Edge             | O(1)               | O(1)                 |
| Check Edge Existence | O(k) (neighbors)   | O(1)                 |
| BFS/DFS              | O(V + E)           | O(V^2)               |

- **V**: Number of vertices
- **E**: Number of edges

### 💡 Tips:

1. **Visited Set:** Always maintain a visited set to avoid infinite loops.
2. **Early Stopping:** For optimization, stop the traversal as soon as you find the target node.
3. **Practice Problem Patterns:**
   - 🔁 **Cycle detection:** Use DFS with parent tracking.
   - 📊 **Shortest Path (Unweighted):** BFS.
   - 🧮 **Shortest Path (Weighted):** Dijkstra's or Bellman-Ford.

### 📌 Example Intuition (Number of Islands):

- Problem: Count the number of disconnected components (islands).
- Approach: Use DFS or BFS starting from each unvisited land cell (`1`), and mark all connected `1`s as visited.

---

## 6. 🔗 Resources and Links

- [Python Graph Documentation](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- [Java Collections Framework](https://docs.oracle.com/javase/8/docs/)
- LeetCode Graph Problems:
  - [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
  - [Course Schedule](https://leetcode.com/problems/course-schedule/)
  - [Number of Islands](https://leetcode.com/problems/number-of-islands/)
  - [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
  - [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
