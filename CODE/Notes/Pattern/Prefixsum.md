
# 🚀 Prefix Sum Pattern Notes

## 📌 What is Prefix Sum?
Prefix Sum is a powerful technique used to preprocess an array for quick range sum queries. It helps optimize problems involving sum calculations over subarrays.

---

## 📚 Key Idea
1. **Precompute prefix sums** to store cumulative sums.
2. **Use prefix sum values** to answer range sum queries efficiently.
3. **Avoid recomputation** by leveraging stored sums.

---

## 🔹 Formula
For an array `arr`:
- **Prefix Sum Array** `prefix[i] = arr[0] + arr[1] + ... + arr[i]`
- **Range Sum Query** for `arr[l:r]`:
  ```
  sum(l, r) = prefix[r] - prefix[l-1]  # If l > 0
  sum(0, r) = prefix[r]                 # If l = 0
  ```

---

## 🐍 Python Implementation
```python
from typing import List

def prefix_sum(arr: List[int]) -> List[int]:
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    
    return prefix

# Example Usage
arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)
print("Prefix Sum Array:", prefix)

# Range Sum Query Example
def range_sum(l: int, r: int, prefix: List[int]) -> int:
    return prefix[r] - (prefix[l-1] if l > 0 else 0)

print("Sum from index 1 to 3:", range_sum(1, 3, prefix))
```

---

## ☕ Java Implementation
```java
import java.util.*;

public class PrefixSum {
    public static int[] prefixSum(int[] arr) {
        int n = arr.length;
        int[] prefix = new int[n];
        prefix[0] = arr[0];
        
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + arr[i];
        }
        
        return prefix;
    }

    public static int rangeSum(int l, int r, int[] prefix) {
        return prefix[r] - (l > 0 ? prefix[l - 1] : 0);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] prefix = prefixSum(arr);
        System.out.println("Prefix Sum Array: " + Arrays.toString(prefix));
        System.out.println("Sum from index 1 to 3: " + rangeSum(1, 3, prefix));
    }
}
```

---

## ⚡ Applications
✅ **Range Sum Queries** (e.g., Sum of subarray in O(1))
✅ **Finding Equilibrium Index** (Sum of left & right subarrays)
✅ **Checking Subarray Conditions** (e.g., Subarray sum = k)
✅ **Difference Arrays** (For efficiently applying range updates)

---

## 🔥 Optimized Usage
- **2D Prefix Sum**: Used for fast sum queries in matrices.
- **Prefix XOR**: Similar concept applied to bitwise XOR operations.
- **Binary Indexed Tree (Fenwick Tree)**: A more dynamic alternative.

📌 Mastering **Prefix Sum** helps in solving problems efficiently in **O(1) Query Time** after **O(N) Preprocessing**. 🚀

