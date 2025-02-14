Here’s a comprehensive set of Markdown notes for **Sorting** and its various techniques:

---

# 🔄 Sorting Techniques

Sorting is the process of arranging data in a specific order, typically ascending or descending. It is a fundamental operation in computer science, often used to optimize searching or organize data.

---

## 🌟 Types of Sorting Techniques

Sorting algorithms can be classified into two main categories:

1. **Comparison-based Sorting:** Elements are compared to each other to determine the order.
2. **Non-comparison Sorting:** Sorting is achieved using other properties of elements (e.g., counting).

---

### 📝 Comparison-Based Sorting Algorithms

### 1. 🃏 **Bubble Sort**

Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.

#### 🔧 Key Points:

- **Time Complexity:**
  - Best Case: \(O(n)\) (already sorted).
  - Worst Case: \(O(n^2)\).
- **Space Complexity:** \(O(1)\) (in-place).
- **Stable Sorting Algorithm:** Yes.

#### 📜 Algorithm:

1. Traverse the array.
2. Compare adjacent elements and swap them if necessary.
3. Repeat for \(n-1\) passes.

#### 📜 Python Code:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

---

### 2. 🔑 **Selection Sort**

Selection Sort repeatedly finds the minimum element and places it in its correct position.

#### 🔧 Key Points:

- **Time Complexity:** \(O(n^2)\) for all cases.
- **Space Complexity:** \(O(1)\).
- **Stable Sorting Algorithm:** No.

#### 📜 Algorithm:

1. Find the minimum element in the unsorted part.
2. Swap it with the first element of the unsorted part.
3. Repeat for the remaining array.

#### 📜 Python Code:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

### 3. 🔄 **Insertion Sort**

Insertion Sort builds the sorted array one element at a time by inserting elements into their correct positions.

#### 🔧 Key Points:

- **Time Complexity:**
  - Best Case: \(O(n)\) (already sorted).
  - Worst Case: \(O(n^2)\).
- **Space Complexity:** \(O(1)\).
- **Stable Sorting Algorithm:** Yes.

#### 📜 Algorithm:

1. Pick the next element.
2. Shift all larger elements one position to the right.
3. Insert the element in its correct position.

#### 📜 Python Code:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

---

### 4. ⚡ **Merge Sort**

Merge Sort is a divide-and-conquer algorithm that divides the array into halves, sorts them, and merges the sorted halves.

#### 🔧 Key Points:

- **Time Complexity:** \(O(n \log n)\) for all cases.
- **Space Complexity:** \(O(n)\).
- **Stable Sorting Algorithm:** Yes.

#### 📜 Algorithm:

1. Divide the array into halves.
2. Recursively sort both halves.
3. Merge the sorted halves.

#### 📜 Python Code:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```

---

### 5. 🔥 **Quick Sort**

Quick Sort is a divide-and-conquer algorithm that selects a pivot, partitions the array, and recursively sorts the partitions.

#### 🔧 Key Points:

- **Time Complexity:**
  - Best/Average Case: \(O(n \log n)\).
  - Worst Case: \(O(n^2)\) (poor pivot choice).
- **Space Complexity:** \(O(\log n)\) (recursion stack).
- **Stable Sorting Algorithm:** No.

#### 📜 Algorithm:

1. Choose a pivot element.
2. Partition the array around the pivot.
3. Recursively apply the same steps to subarrays.

#### 📜 Python Code:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

### 📝 Non-Comparison Sorting Algorithms

### 1. 🧮 **Counting Sort**

Counting Sort works by counting the occurrences of each element and using this information to place elements in the sorted order.

#### 🔧 Key Points:

- **Time Complexity:** \(O(n + k)\), where \(k\) is the range of input.
- **Space Complexity:** \(O(k)\).
- **Stable Sorting Algorithm:** Yes.

#### 📜 Algorithm:

1. Count occurrences of each element.
2. Compute cumulative counts.
3. Place elements in the sorted order based on counts.

#### 📜 Python Code:

```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)

    return sorted_arr
```

---

## 📊 Comparison of Sorting Algorithms

| Algorithm      | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity | Stable? |
| -------------- | ---------------------- | ----------------------- | ---------------- | ------- |
| Bubble Sort    | \(O(n)\)               | \(O(n^2)\)              | \(O(1)\)         | Yes     |
| Selection Sort | \(O(n^2)\)             | \(O(n^2)\)              | \(O(1)\)         | No      |
| Insertion Sort | \(O(n)\)               | \(O(n^2)\)              | \(O(1)\)         | Yes     |
| Merge Sort     | \(O(n \log n)\)        | \(O(n \log n)\)         | \(O(n)\)         | Yes     |
| Quick Sort     | \(O(n \log n)\)        | \(O(n^2)\)              | \(O(\log n)\)    | No      |
| Counting Sort  | \(O(n + k)\)           | \(O(n + k)\)            | \(O(k)\)         | Yes     |

---

## 🎯 Tips for Sorting in Interviews

1. **Understand the input constraints**:
   - Use **Counting Sort** for small, integer-based inputs.
   - Use **Merge Sort** for guaranteed \(O(n \log n)\) sorting.
2. **Optimize for space**:
   - Use **Quick Sort** or **Heap Sort** for in-place sorting.
3. **Practice problems**:
   - Sorting and searching problems on arrays.
   - Implementing custom comparators.

---

Let me know if you'd like more details or examples added to this! 🚀
