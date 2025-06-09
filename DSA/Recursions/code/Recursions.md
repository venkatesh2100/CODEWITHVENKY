# Recursion Notes 📖

## Introduction to Recursion 🔄

Recursion is a method where the solution to a problem depends on solving smaller instances of the same problem. A recursive function calls itself within its definition.

### Key Properties of Recursion 🧐

1. **Base Case (Stopping Condition) 🚦** - The function should have a condition to stop the recursion.
2. **Recursive Case 🔄** - The function calls itself with modified arguments.
3. **Convergence 🛑** - The input should get closer to the base case.

## Types of Recursion 🏗️

### 1️⃣ Direct Recursion

When a function calls itself directly.

```python
# Example: Factorial of a number using Direct Recursion

def factorial(n):
    if n == 0 or n == 1:  # Base Case
        return 1
    return n * factorial(n - 1)  # Recursive Case

print(factorial(5))  # Output: 120
```

### 2️⃣ Indirect Recursion

When two or more functions call each other in a cycle.

```python
# Example: Indirect Recursion

def even(n):
    if n == 0:
        return True
    return odd(n - 1)

def odd(n):
    if n == 0:
        return False
    return even(n - 1)

print(even(10))  # Output: True
print(odd(11))   # Output: True
```

### 3️⃣ Tail Recursion

When the recursive call is the last operation before returning a result.

```python
# Example: Tail Recursion for Factorial

def tail_factorial(n, acc=1):
    if n == 0:
        return acc
    return tail_factorial(n - 1, n * acc)

print(tail_factorial(5))  # Output: 120
```

**Why use Tail Recursion?**

- Optimized by compilers to avoid stack overflow.
- Converts into iteration internally.

### 4️⃣ Head Recursion

The recursive call happens first, before any other operations.

```python
# Example: Head Recursion

def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print(n, end=' ')

head_recursion(5)  # Output: 1 2 3 4 5
```

### 5️⃣ Tree Recursion 🌳

When a function makes multiple recursive calls.

```python
# Example: Fibonacci using Tree Recursion

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8
```

⚠️ **Drawback**: Recomputes values multiple times, leading to inefficiency.

### 6️⃣ Nested Recursion 🏗️

When the recursive function's argument is a recursive function itself.

```python
# Example: Nested Recursion

def nested(n):
    if n > 100:
        return n - 10
    return nested(nested(n + 11))

print(nested(95))  # Output: 91
```

## Recursion vs Iteration 🔄➡️⏩

| Feature        | Recursion                          | Iteration                   |
| -------------- | ---------------------------------- | --------------------------- |
| Memory Usage   | High (uses call stack)             | Low (uses loops)            |
| Performance    | Can be slow (without optimization) | Generally faster            |
| Readability    | More readable for complex problems | Can be harder to understand |
| Function Calls | Multiple                           | Single                      |

## Recursion Optimization Techniques ⚡

### 1️⃣ Memoization (Top-Down DP)

Stores previously computed results to avoid redundant calculations.

```python
# Example: Fibonacci using Memoization

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(10))  # Output: 55
```

### 2️⃣ Tabulation (Bottom-Up DP)

Builds solutions iteratively from the smallest subproblems.

```python
# Example: Fibonacci using Tabulation

def fibonacci(n):
    dp = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibonacci(10))  # Output: 55
```

### 3️⃣ Tail Recursion Optimization

Converts recursion into iteration.

## When to Use Recursion? ✅

- **Tree-based problems** (DFS, Binary Trees, etc.) 🌲
- **Divide & Conquer algorithms** (Merge Sort, Quick Sort) 🔪
- **Backtracking problems** (N-Queens, Sudoku Solver) ♟️
- **Graph traversal** (DFS, BFS) 🌐

## When to Avoid Recursion? ❌

- When memory usage is a concern 📉
- When an iterative solution is more efficient ⏩
- When deep recursion leads to stack overflow 🚨

## Conclusion 🎯

Recursion is a powerful technique used in many algorithmic problems. Understanding different types of recursion and optimizing it using techniques like **memoization and tail recursion** can make a huge difference in performance!

---

Happy Coding! 🚀
