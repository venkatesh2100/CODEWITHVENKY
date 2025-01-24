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
    Here’s an expanded outline with subtopics and explanations for **Topological Sort**, **DFS**, and **BFS** in Markdown format:

---

# 🕸️ Graph Traversal Techniques

## 1. 🔄 Depth-First Search (DFS)

DFS is a graph traversal algorithm that explores as far as possible down a branch before backtracking.

### 🧩 Key Points:

- **Traversal Order:** Explore all neighbors of the current node, then move deeper before backtracking.
- **Approach:** Implemented recursively or iteratively using a stack.
- **Applications:**
  - Detecting cycles.
  - Finding connected components.
  - Topological sorting (in directed acyclic graphs).
  - Solving maze problems.

### 🛠️ Algorithm:

1. Start at a node.
2. Mark it as visited.
3. Recursively visit all unvisited neighbors.

### ⏱️ Time Complexity:

- **Adjacency List:** \( O(V + E) \) (Vertices + Edges)
- **Adjacency Matrix:** \( O(V^2) \)

### 📜 Python Code:

```python
def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}
visited = set()
dfs(graph, 0, visited)
```

### 📜 Java Code:

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

## 2. 🚀 Breadth-First Search (BFS)

BFS is a graph traversal algorithm that explores all neighbors of the current node before moving to the next level.

### 🧩 Key Points:

- **Traversal Order:** Level by level (or breadth-wise).
- **Approach:** Implemented using a queue.
- **Applications:**
  - Shortest path in an unweighted graph.
  - Checking bipartite graphs.
  - Flood-fill algorithms (e.g., "Number of Islands").

### 🛠️ Algorithm:

1. Start at a node.
2. Add it to the queue and mark it as visited.
3. Dequeue a node and explore all its neighbors.

### ⏱️ Time Complexity:

- **Adjacency List:** \( O(V + E) \)
- **Adjacency Matrix:** \( O(V^2) \)

### 📜 Python Code:

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

### 📜 Java Code:

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

---

## 3. 📊 Topological Sort

Topological sort is a linear ordering of vertices in a **Directed Acyclic Graph (DAG)** such that for every directed edge \( u \to v \), vertex \( u \) comes before \( v \).

### 🧩 Key Points:

- **Traversal Order:** Linear ordering of vertices.
- **Approach:** Can be implemented using:
  - **DFS** with a stack.
  - **Kahn's Algorithm** (BFS-based).
- **Applications:**
  - Task scheduling.
  - Course dependency problems (e.g., "Course Schedule" on LeetCode).

### 🛠️ Algorithm (DFS-Based):

1. Use a stack to store nodes in reverse order of their finishing time.
2. Visit unvisited nodes using DFS and push them onto the stack after exploring all their neighbors.
3. Reverse the stack to get the topological order.

### 🛠️ Algorithm (Kahn's Algorithm):

1. Calculate in-degrees of all nodes.
2. Use a queue to add nodes with zero in-degrees.
3. Remove nodes from the queue, reducing in-degrees of their neighbors.
4. Add neighbors with zero in-degrees to the queue.

### ⏱️ Time Complexity:

- **DFS-Based:** \( O(V + E) \)
- **Kahn’s Algorithm:** \( O(V + E) \)

### 📜 Python Code (DFS-Based):

```python
def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            stack.append(node)

    for node in graph:
        dfs(node)

    return stack[::-1]  # Reverse the stack for topological order

# Example
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}
print(topological_sort_dfs(graph))
```

### 📜 Python Code (Kahn’s Algorithm):

```python
from collections import deque

def topological_sort_kahn(graph, num_nodes):
    in_degree = {i: 0 for i in range(num_nodes)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == num_nodes else []

# Example
graph = {0: [1, 2], 1: [2], 2: [3], 3: []}
print(topological_sort_kahn(graph, 4))
```

---

## 4. 🛠️ How to Choose Between BFS, DFS, and Topological Sort?

| **Scenario**                         | **Algorithm**    |
| ------------------------------------ | ---------------- |
| Shortest path in an unweighted graph | BFS              |
| Detect cycles in a directed graph    | DFS              |
| Find connected components            | DFS              |
| Level-order traversal                | BFS              |
| Task scheduling                      | Topological Sort |
| Solve maze problems                  | DFS              |
| Large sparse graphs                  | DFS              |

---

## 5. 🎯 Tips for Graph Problems in Interviews

1. **Understand the Graph Type:** Is it directed, undirected, weighted, or unweighted?
2. **Practice Common Patterns:**
   - Cycle detection.
   - Connected components.
   - Topological sorting.
3. **Optimize for Constraints:**
   - For \( n < 1000 \): Recursive DFS or adjacency matrix.
   - For large, sparse graphs: Adjacency list with BFS/DFS.
4. **Track Visited Nodes:** Always maintain a `visited` set to avoid infinite loops.

---

Let me know if you'd like to expand on specific sections or need further clarification! 🚀 - [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
