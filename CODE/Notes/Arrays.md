
# Arrays

Arrays are one of the fundamental data structures in computer science, used to store multiple values in a single variable. Understanding various algorithms, tips, and tricks for arrays is crucial for efficient problem-solving.

---

## ✨ Key Concepts

### 1. **Definition**
An array is a collection of elements stored at contiguous memory locations. Elements in an array are accessed using an index.

### 2. **Types of Arrays**
- **One-Dimensional Arrays** (1D)
- **Multi-Dimensional Arrays** (2D, 3D, etc.)
- **Jagged Arrays** (arrays of varying lengths)

### 3. **Common Operations**
- Accessing elements (`O(1)`) 
- Insertion (`O(n)`) 
- Deletion (`O(n)`) 
- Searching (`O(n) or O(log n)`) 
- Sorting (`O(n log n)`) 

---

## 🌟 Array Algorithms and Tricks

### 1. **Searching Algorithms**
#### Linear Search (`O(n)`) - Simple but slow for large arrays.
#### Binary Search (`O(log n)`) - Requires sorted array.
```python
# Python Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
```java
// Java Binary Search
class Solution {
    public int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
}
```

### 2. **Sorting Algorithms**
- **Bubble Sort** (`O(n²)`) - Simple but inefficient.
- **Merge Sort** (`O(n log n)`) - Divide and conquer.
- **Quick Sort** (`O(n log n)`) - Efficient but unstable.
- **Counting Sort** (`O(n + k)`) - Good for small ranges.

```python
# Quick Sort in Python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

### 3. **Kadane's Algorithm (Max Subarray Sum)**
```python
# Python Kadane's Algorithm
def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```
```java
// Java Kadane's Algorithm
class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0], currentSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }
}
```

### 4. **Two-Pointer Technique**
Used in problems like sorting, searching, and pairs/sum problems.
```python
# Python Two Sum Problem
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        sum_ = arr[left] + arr[right]
        if sum_ == target:
            return [left, right]
        elif sum_ < target:
            left += 1
        else:
            right -= 1
    return []
```

### 5. **Sliding Window Technique**
Used for optimizing contiguous subarray problems.
```python
# Python Sliding Window (Max Sum of K elements)
def max_sum_subarray(arr, k):
    max_sum = sum(arr[:k])
    current_sum = max_sum
    for i in range(len(arr) - k):
        current_sum = current_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, current_sum)
    return max_sum
```

---

## 📊 Complexity Analysis
| Algorithm       | Best Case | Worst Case |
|----------------|-----------|------------|
| Linear Search  | O(1)      | O(n)       |
| Binary Search  | O(1)      | O(log n)   |
| Quick Sort     | O(n log n)| O(n²)      |
| Merge Sort     | O(n log n)| O(n log n) |
| Kadane's Algo  | O(n)      | O(n)       |

---

## 🚀 Summary
Arrays are essential in problem-solving. Understanding searching, sorting, and optimization techniques like Two Pointers and Sliding Window is crucial for efficient algorithms!

