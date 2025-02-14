
# Backtracking 

Backtracking is a general algorithmic technique that involves searching for a solution incrementally, abandoning a path as soon as it is determined that it cannot yield a valid solution. It is commonly used in problems involving permutations, combinations, and constraint satisfaction.

---

## ✨ Key Concepts

### 1. **Definition**
Backtracking is a depth-first search (DFS) approach where we explore possible solutions and backtrack when we reach an invalid state.

### 2. **When to Use Backtracking?**
- When the problem requires finding all possible solutions.
- When the solution space is large but can be pruned.
- When a problem involves constraints (e.g., Sudoku, N-Queens).
- When a brute-force approach is inefficient.

### 3. **Backtracking Framework**
1. Choose a possible solution.
2. Recursively explore further.
3. If an invalid solution is found, **backtrack** and try a different path.

---

## 🌱 Types of Backtracking Approaches

### 1. **Decision Tree Backtracking**
   - Used when choosing elements from a given set.
   - Example: Generating permutations, subsets, combinations.

### 2. **Constraint-Based Backtracking**
   - Used in problems like N-Queens and Sudoku where solutions must satisfy constraints.
   
### 3. **Optimized Backtracking (Pruning)**
   - Uses additional conditions to reduce the number of recursive calls.
   - Example: Branch and Bound technique.

---

## 🌟 Backtracking Algorithms and Examples

### 1. **Subset Generation (Power Set)**
#### Python Code:
```python
class Solution:
    def subsets(self, nums):
        res = []
        def backtrack(start, path):
            res.append(path[:])  # Store the subset
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack
        backtrack(0, [])
        return res
```

#### Java Code:
```java
import java.util.*;
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(0, nums, new ArrayList<>(), res);
        return res;
    }
    private void backtrack(int start, int[] nums, List<Integer> path, List<List<Integer>> res) {
        res.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(i + 1, nums, path, res);
            path.remove(path.size() - 1);
        }
    }
}
```

### 2. **Permutations**
#### Python Code:
```python
class Solution:
    def permute(self, nums):
        res = []
        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        backtrack([], nums)
        return res
```

#### Java Code:
```java
import java.util.*;
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(new ArrayList<>(), nums, new boolean[nums.length], res);
        return res;
    }
    private void backtrack(List<Integer> path, int[] nums, boolean[] used, List<List<Integer>> res) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.add(nums[i]);
            backtrack(path, nums, used, res);
            path.remove(path.size() - 1);
            used[i] = false;
        }
    }
}
```

### 3. **N-Queens Problem**
#### Python Code:
```python
class Solution:
    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]
        def is_safe(row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                    return False
                if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
                    return False
            return True
        
        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
        backtrack(0)
        return res
```

#### Java Code:
```java
import java.util.*;
class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        char[][] board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        backtrack(0, board, res);
        return res;
    }
    private void backtrack(int row, char[][] board, List<List<String>> res) {
        if (row == board.length) {
            res.add(construct(board));
            return;
        }
        for (int col = 0; col < board.length; col++) {
            if (isSafe(row, col, board)) {
                board[row][col] = 'Q';
                backtrack(row + 1, board, res);
                board[row][col] = '.';
            }
        }
    }
    private boolean isSafe(int row, int col, char[][] board) {
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
            if (col - (row - i) >= 0 && board[i][col - (row - i)] == 'Q') return false;
            if (col + (row - i) < board.length && board[i][col + (row - i)] == 'Q') return false;
        }
        return true;
    }
    private List<String> construct(char[][] board) {
        List<String> result = new ArrayList<>();
        for (char[] row : board) result.add(new String(row));
        return result;
    }
}
```

---

## 📊 Complexity Analysis
- **Worst Case:** `O(N!)` for permutation problems.
- **Optimized Cases:** Using pruning, constraints, and memoization.

---

## 🚀 Summary
Backtracking is a powerful technique that solves combinatorial problems efficiently. Mastering recursion and pruning strategies helps in optimizing backtracking solutions!

