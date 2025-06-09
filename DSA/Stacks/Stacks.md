# 📚 Stack - Interview Preparation Guide

## 🔹 What is a Stack?
A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.
- 🔼 **Push**: Add an element to the top of the stack.
- 🔽 **Pop**: Remove the top element from the stack.
- 👀 **Peek (Top)**: View the top element without removing it.
- 📏 **IsEmpty**: Check if the stack is empty.

## 🏗️ Stack Operations and Their Complexity
| Operation | Time Complexity |
|-----------|----------------|
| Push      | O(1) |
| Pop       | O(1) |
| Peek      | O(1) |
| Search    | O(n) |

## 🛠️ Implementing Stack
### Python (Using `list`)
```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
```

### Java (Using `Stack` class)
```java
import java.util.Stack;

public class StackExample {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println("Top: " + stack.peek()); // 3
        stack.pop();
        System.out.println("After Pop: " + stack.peek()); // 2
    }
}
```

---

## 💡 Stack-Based Problems and Solutions

### 1️⃣ **Valid Parentheses** (Leetcode #20)
**Problem**: Given a string of brackets `"(){}[]"`, check if it is valid.

🔹 **Algorithm:**
1. Use a stack to store opening brackets.
2. For each closing bracket, check if the top of the stack matches.
3. If stack is empty at the end, return `True`.

🔹 **Python Solution:**
```python
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
```

🔹 **Java Solution:**
```java
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = Map.of(')', '(', '}', '{', ']', '[');
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                char top = stack.isEmpty() ? '#' : stack.pop();
                if (top != map.get(c)) return false;
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
```

### 2️⃣ **Next Greater Element** (Leetcode #496)
**Problem**: Given an array, find the next greater element for each element.

🔹 **Algorithm:**
- Use a **monotonic decreasing stack**.
- Traverse array from **right to left**.
- Keep popping elements from the stack that are **smaller** than the current element.

🔹 **Python Solution:**
```python
def nextGreaterElement(nums):
    stack, res = [], [-1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res
```

🔹 **Java Solution:**
```java
import java.util.*;

class Solution {
    public int[] nextGreaterElement(int[] nums) {
        int[] res = new int[nums.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums[i]) {
                stack.pop();
            }
            res[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(nums[i]);
        }
        return res;
    }
}
```

### 3️⃣ **Daily Temperatures** (Leetcode #739)
**Problem**: Find the number of days you have to wait for a **warmer** temperature.

🔹 **Python Solution:**
```python
def dailyTemperatures(T):
    stack, res = [], [0] * len(T)
    for i, temp in enumerate(T):
        while stack and T[stack[-1]] < temp:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)
    return res
```

🔹 **Java Solution:**
```java
class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] res = new int[T.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < T.length; i++) {
            while (!stack.isEmpty() && T[stack.peek()] < T[i]) {
                int prev = stack.pop();
                res[prev] = i - prev;
            }
            stack.push(i);
        }
        return res;
    }
}
```

---

## 🔥 **Tips for Solving Stack Problems**
1. **Think about LIFO** – If the problem involves backtracking or undoing, stacks are a good choice.
2. **Monotonic Stacks** – Used for problems like "Next Greater Element" and "Stock Span Problem".
3. **Use a Stack to Track Indices** – Useful for problems where you need to compare past elements (e.g., "Daily Temperatures").
4. **Watch Out for Edge Cases** – Empty stacks, single elements, and duplicate values.
5. **Optimize with One Pass** – Many stack problems can be solved in **O(n)** with a single loop.

---

## 🎯 **Final Thoughts**
Stacks are a fundamental **data structure** used in many real-world applications, from parsing expressions to handling undo operations. Mastering stacks will give you an edge in technical interviews! 🚀

Happy coding! 😃🔥

