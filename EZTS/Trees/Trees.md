# 🌳 **Trees in Data Structures and Algorithms (DSA)**

## 🔍 **Introduction to Trees**

A **Tree** is a hierarchical data structure consisting of nodes connected by edges. It is a non-linear data structure that simulates a hierarchical tree structure with a root node and child nodes.

### 🌟 **Properties of Trees**
- **Root**: The topmost node of a tree.
- **Parent**: A node connected above a given node.
- **Child**: A node connected below a given node.
- **Leaf Node**: A node with no children.
- **Edge**: Connection between two nodes.
- **Depth**: Distance from the root node to a given node.
- **Height**: Longest path from a node to a leaf.
- **Subtree**: A tree formed by any node and its descendants.

### 🔗 **Types of Trees**
- **Binary Tree**: Each node has at most 2 children.
- **Binary Search Tree (BST)**: Left child < parent < right child.
- **AVL Tree**: Self-balancing BST with a height difference of at most 1.
- **Red-Black Tree**: A balanced BST with extra coloring properties.
- **Heap Tree**: Complete binary tree (Min-Heap/Max-Heap).
- **Trie (Prefix Tree)**: Used for efficient searching of words.
- **Segment Tree**: For range queries and updates.
- **Fenwick Tree (Binary Indexed Tree)**: Efficient for cumulative frequency calculations.

---

## ⚒️ **Tree Traversal Techniques**

### 🌿 **Depth-First Search (DFS)**
1. **Pre-order Traversal** (Root ➔ Left ➔ Right)
2. **In-order Traversal** (Left ➔ Root ➔ Right) *(For BST, returns sorted order)*
3. **Post-order Traversal** (Left ➔ Right ➔ Root)

**Example (In-order Traversal):**
```python
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def in_order(root):
    if root:
        in_order(root.left)
        print(root.value, end=' ')
        in_order(root.right)
```

### 🌐 **Breadth-First Search (BFS) or Level-Order Traversal**
- Uses a queue data structure to traverse level by level.

**Example:**
```python
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## 📐 **Operations on Binary Search Tree (BST)**

### ➕ **Insertion**
- Place smaller elements in the left subtree.
- Place larger elements in the right subtree.

### ❌ **Deletion**
- **No child**: Simply remove.
- **One child**: Remove and link the child to the parent.
- **Two children**: Replace with in-order successor or predecessor.

### 🔍 **Searching**
- Time Complexity: O(log n) for balanced BST, O(n) for skewed BST.

---

## 🎯 **Advanced Tree Techniques**

### 🌿 **Balanced Trees**
- **AVL Tree**
  - Maintains a height balance factor of -1, 0, or 1.
  - Rotations: Left, Right, Left-Right, Right-Left.

- **Red-Black Tree Rules:**
  1. Every node is red or black.
  2. The root is always black.
  3. No two consecutive red nodes.
  4. Every path from a node to a null child has the same number of black nodes.

### 📊 **Heap Trees**
- **Max-Heap**: Parent node is greater than its children.
- **Min-Heap**: Parent node is smaller than its children.

**Applications:** Priority queues, heap sort.

### 📜 **Trie (Prefix Tree)**
- Efficient for searching and auto-complete functionalities.

**Example:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
```

### 📈 **Segment Tree**
- Used for range queries (e.g., sum, min, max).
- Time complexity for both queries and updates: O(log n)

### ⚡ **Fenwick Tree (Binary Indexed Tree)**
- Efficient for cumulative frequency table updates.
- Time complexity: O(log n) for updates and queries.

---

## 📊 **Complexity Analysis**
| Operation | Binary Tree | BST | AVL Tree | Red-Black Tree | Heap |
|-----------|-------------|-----|----------|----------------|------|
| Search    | O(n)        | O(log n)* | O(log n) | O(log n) | O(n) |
| Insert    | O(n)        | O(log n)* | O(log n) | O(log n) | O(log n) |
| Delete    | O(n)        | O(log n)* | O(log n) | O(log n) | O(log n) |

*(For balanced BSTs like AVL or Red-Black Trees, search time remains O(log n))*

---

## 💡 **Applications of Trees**
- **Binary Search Tree**: Efficient searching and sorting.
- **Heaps**: Priority queues and scheduling algorithms.
- **Trie**: Auto-complete, spell-checkers.
- **Segment Tree**: Range queries in competitive programming.
- **Fenwick Tree**: Efficient cumulative queries.

---

## 🔥 **Tips for Interview Preparation**
1. Master tree traversals (DFS, BFS).
2. Understand how to balance trees (AVL, Red-Black).
3. Practice insertion, deletion, and search operations in BST.
4. Implement segment trees and tries for advanced problems.
5. Solve real interview problems on platforms like LeetCode or GeeksforGeeks.

---

Happy Coding! 🚀

# 🌳 **Trees in Data Structures and Algorithms (DSA)**

## 🔍 **Introduction to Trees**

A **Tree** is a hierarchical data structure consisting of nodes connected by edges. It is a non-linear data structure that simulates a hierarchical tree structure with a root node and child nodes.

### 🌟 **Properties of Trees**
- **Root**: The topmost node of a tree.
- **Parent**: A node connected above a given node.
- **Child**: A node connected below a given node.
- **Leaf Node**: A node with no children.
- **Edge**: Connection between two nodes.
- **Depth**: Distance from the root node to a given node.
- **Height**: Longest path from a node to a leaf.
- **Subtree**: A tree formed by any node and its descendants.

### 🔗 **Types of Trees**
- **Binary Tree**: Each node has at most 2 children.
- **Binary Search Tree (BST)**: Left child < parent < right child.
- **AVL Tree**: Self-balancing BST with a height difference of at most 1.
- **Red-Black Tree**: A balanced BST with extra coloring properties.
- **Heap Tree**: Complete binary tree (Min-Heap/Max-Heap).
- **Trie (Prefix Tree)**: Used for efficient searching of words.
- **Segment Tree**: For range queries and updates.
- **Fenwick Tree (Binary Indexed Tree)**: Efficient for cumulative frequency calculations.

---

## ⚒️ **Tree Traversal Techniques**

### 🌿 **Depth-First Search (DFS)**
1. **Pre-order Traversal** (Root ➔ Left ➔ Right)
2. **In-order Traversal** (Left ➔ Root ➔ Right) *(For BST, returns sorted order)*
3. **Post-order Traversal** (Left ➔ Right ➔ Root)

**Example (In-order Traversal):**
```python
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def in_order(root):
    if root:
        in_order(root.left)
        print(root.value, end=' ')
        in_order(root.right)
```

### 🌐 **Breadth-First Search (BFS) or Level-Order Traversal**
- Uses a queue data structure to traverse level by level.

**Example:**
```python
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## 📐 **Operations on Binary Search Tree (BST)**

### ➕ **Insertion**
- Place smaller elements in the left subtree.
- Place larger elements in the right subtree.

### ❌ **Deletion**
- **No child**: Simply remove.
- **One child**: Remove and link the child to the parent.
- **Two children**: Replace with in-order successor or predecessor.

### 🔍 **Searching**
- Time Complexity: O(log n) for balanced BST, O(n) for skewed BST.

---

## 🎯 **Advanced Tree Techniques**

### 🌿 **Balanced Trees**
- **AVL Tree**
  - Maintains a height balance factor of -1, 0, or 1.
  - Rotations: Left, Right, Left-Right, Right-Left.

- **Red-Black Tree Rules:**
  1. Every node is red or black.
  2. The root is always black.
  3. No two consecutive red nodes.
  4. Every path from a node to a null child has the same number of black nodes.

### 📊 **Heap Trees**
- **Max-Heap**: Parent node is greater than its children.
- **Min-Heap**: Parent node is smaller than its children.

**Applications:** Priority queues, heap sort.

### 📜 **Trie (Prefix Tree)**
- Efficient for searching and auto-complete functionalities.

**Example:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
```

### 📈 **Segment Tree**
- Used for range queries (e.g., sum, min, max).
- Time complexity for both queries and updates: O(log n)

### ⚡ **Fenwick Tree (Binary Indexed Tree)**
- Efficient for cumulative frequency table updates.
- Time complexity: O(log n) for updates and queries.

---

## 📊 **Complexity Analysis**
| Operation | Binary Tree | BST | AVL Tree | Red-Black Tree | Heap |
|-----------|-------------|-----|----------|----------------|------|
| Search    | O(n)        | O(log n)* | O(log n) | O(log n) | O(n) |
| Insert    | O(n)        | O(log n)* | O(log n) | O(log n) | O(log n) |
| Delete    | O(n)        | O(log n)* | O(log n) | O(log n) | O(log n) |

*(For balanced BSTs like AVL or Red-Black Trees, search time remains O(log n))*

---

## 💡 **Applications of Trees**
- **Binary Search Tree**: Efficient searching and sorting.
- **Heaps**: Priority queues and scheduling algorithms.
- **Trie**: Auto-complete, spell-checkers.
- **Segment Tree**: Range queries in competitive programming.
- **Fenwick Tree**: Efficient cumulative queries.

---

## 🔥 **Tips for Interview Preparation**
1. Master tree traversals (DFS, BFS).
2. Understand how to balance trees (AVL, Red-Black).
3. Practice insertion, deletion, and search operations in BST.
4. Implement segment trees and tries for advanced problems.
5. Solve real interview problems on platforms like LeetCode or GeeksforGeeks.

---

Happy Coding! 🚀

