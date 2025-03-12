Here’s a well-structured **Sliding Window Interview Prep Notes** in Markdown format (`.md`) with **Python & Java** code, along with **emojis** for better readability. 🚀  

---

### **📌 Sliding Window - Interview Prep Notes**
> **🔹 Sliding Window** is an **optimized** approach used for problems that involve **contiguous subarrays, substrings, or sequences**. Instead of checking all possibilities, it **slides a window** over the input to reduce **time complexity**.

---

## **🛠 Types of Sliding Window**
1️⃣ **Fixed-Size Window** → The window size remains **constant**.  
2️⃣ **Variable-Size Window** → The window size **adjusts** based on conditions.  

---

## **🔹 When to Use Sliding Window?**
✅ **Subarray / substring problems**  
✅ **Finding max/min sum in k elements**  
✅ **Problems with contiguous elements**  
✅ **Optimizing brute-force approaches (`O(n^2) → O(n)`)**  

---

## **🚀 Fixed-Size Sliding Window**
> **Problem:** Find the **maximum sum of `k` consecutive elements** in an array.

### **📝 Approach**
1️⃣ Compute the **sum** of the first `k` elements.  
2️⃣ **Slide** the window by adding the next element & removing the first element.  
3️⃣ Keep track of the **maximum sum**.  

### **💻 Python Code**
```python
def max_sum_subarray(nums, k):
    max_sum = float('-inf')
    curr_sum = sum(nums[:k])

    for i in range(len(nums) - k):
        curr_sum = curr_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum
```

### **☕ Java Code**
```java
class SlidingWindow {
    public static int maxSumSubarray(int[] nums, int k) {
        int maxSum = Integer.MIN_VALUE;
        int currSum = 0;

        for (int i = 0; i < k; i++) {
            currSum += nums[i];
        }

        for (int i = k; i < nums.length; i++) {
            currSum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, currSum);
        }

        return maxSum;
    }
}
```

🔹 **Time Complexity:** `O(n)` ✅  
🔹 **Space Complexity:** `O(1)` ✅  

---

## **🚀 Variable-Size Sliding Window**
> **Problem:** Find the **smallest subarray with sum ≥ `S`**.

### **📝 Approach**
1️⃣ Use two pointers: **left** & **right**.  
2️⃣ Expand the window by moving `right` until sum ≥ `S`.  
3️⃣ Try **shrinking** the window from `left` to get the **minimum length**.  

### **💻 Python Code**
```python
def min_subarray_len(nums, s):
    left = 0
    curr_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= s:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0
```

### **☕ Java Code**
```java
class SlidingWindow {
    public static int minSubArrayLen(int s, int[] nums) {
        int left = 0, sum = 0, minLen = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];

            while (sum >= s) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left++];
            }
        }

        return (minLen == Integer.MAX_VALUE) ? 0 : minLen;
    }
}
```

🔹 **Time Complexity:** `O(n)` ✅  
🔹 **Space Complexity:** `O(1)` ✅  

---

## **📝 Common Sliding Window Problems**
| **Problem** | **Type** | **Description** |
|------------|----------|----------------|
| **Max sum of `k` consecutive elements** | Fixed Window | Find the max sum of `k` elements |
| **Longest substring without repeating characters** | Variable Window | Find the longest substring with unique characters |
| **Smallest subarray with sum ≥ `S`** | Variable Window | Find the shortest subarray with sum ≥ `S` |
| **Longest subarray with at most `k` distinct numbers** | Variable Window | Find the longest subarray with ≤ `k` distinct elements |
| **Maximum number of vowels in `k` length substring** | Fixed Window | Count the max vowels in a `k` length substring |

---

## **🚀 Tips for Sliding Window in Interviews**
✅ Use **two pointers (`left`, `right`)**  
✅ Think about **shrinking or expanding** the window  
✅ Use **HashMap / Frequency Map** for substring problems  
✅ If a problem involves **contiguous elements**, think **Sliding Window**!  

---

### **🔹 Conclusion**
✅ **Sliding Window** is a powerful technique that reduces time complexity from `O(n^2)` to `O(n)`.  
✅ It is highly useful for **subarray/substring problems**.  
✅ Understanding **fixed** and **variable** window problems is crucial for **coding interviews**.  

🔥 **Master Sliding Window to ace interviews!** 🚀  

---

Would you like additional variations or explanations? 😊
