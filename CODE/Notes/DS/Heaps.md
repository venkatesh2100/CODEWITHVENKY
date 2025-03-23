
# Heaps - Interview Prep

## 📌 Introduction to Heaps
A **Heap** is a special type of **binary tree** that satisfies the **heap property**:
- **Max-Heap**: The parent node is always **greater** than or equal to its children.
- **Min-Heap**: The parent node is always **smaller** than or equal to its children.

Heaps are commonly used to implement **Priority Queues** and are useful in many algorithms like **Heap Sort, Dijkstra's Algorithm, and Prim's Algorithm**.

---

## 🏗️ Types of Heaps

### 1️⃣ **Max Heap**
- Root node contains the **maximum** value.
- Every parent node is **greater** than or equal to its children.

### 2️⃣ **Min Heap**
- Root node contains the **minimum** value.
- Every parent node is **smaller** than or equal to its children.

---

## 🔥 Heap Operations

### **1. Insertion (O(log N))**
1. Insert the new element at the **end**.
2. **Heapify Up**: Compare with its parent and swap if necessary.

### **2. Deletion (O(log N))**
1. Replace the root with the **last element**.
2. **Heapify Down**: Compare with children and swap with the smallest/largest.

### **3. Heapify (O(N))**
Convert an unsorted array into a valid heap by calling `heapify()` from bottom to top.

---

## ⚡ Implementation in C++
### **Using `priority_queue` (Max Heap by Default)**
```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int> maxHeap; // Max Heap
    maxHeap.push(10);
    maxHeap.push(40);
    maxHeap.push(30);
    maxHeap.push(20);

    cout << "Top Element (Max): " << maxHeap.top() << endl; // 40
    maxHeap.pop();
    cout << "Next Max: " << maxHeap.top() << endl; // 30

    return 0;
}
```

### **Min Heap using `priority_queue`**
```cpp
priority_queue<int, vector<int>, greater<int>> minHeap;
```

### **Custom Comparator in C++**
```cpp
struct Compare {
    bool operator()(int a, int b) {
        return a > b; // Min Heap
    }
};
priority_queue<int, vector<int>, Compare> customMinHeap;
```

---

## ⚡ Implementation in Python
### **Using `heapq` (Min Heap by Default)**
```python
import heapq

min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 40)
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 20)

print("Min Element:", heapq.heappop(min_heap)) # 10
print("Next Min:", min_heap[0]) # 20
```

### **Max Heap using `heapq`**
```python
max_heap = []
heapq.heappush(max_heap, -10)  # Store negative values
heapq.heappush(max_heap, -40)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -20)

print("Max Element:", -heapq.heappop(max_heap)) # 40
```

---

## 🚀 Applications of Heaps
- **Priority Queues**
- **Heap Sort** (O(N log N))
- **Dijkstra’s Algorithm** (Shortest Path)
- **Prim’s Algorithm** (Minimum Spanning Tree)
- **Top K Elements in a Stream**
- **Merging K Sorted Lists**

---

## 🔥 Heap Sort Algorithm (C++)
```cpp
void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
```

---

## 🔥 Heap Sort Algorithm (Python)
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```

---

## 📝 Summary
- **Heap is a complete binary tree.**
- **Used for priority queues and efficient sorting.**
- **Python's `heapq` is a Min Heap by default.**
- **C++ `priority_queue` is a Max Heap by default.**
- **Heapify takes O(N) time, insertion & deletion take O(log N).**

🔥 Mastering heaps will help in competitive programming and real-world applications!
