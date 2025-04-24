
# 🧠 Bit Manipulation in DSA (Advanced Notes for Interview Prep)

Bit manipulation refers to the algorithmic technique of using bitwise operators to solve problems more efficiently, especially in space/time-critical applications like competitive programming and systems design.

---

## 📅 Table of Contents
1. Bitwise Operators
2. Binary Representations and Number Systems
3. Common Bit Manipulation Techniques
4. Advanced Bit Tricks and Patterns
5. Real-world DSA Applications
6. Bitmasking and Subset Enumeration
7. Bit Manipulation Problems for Practice

---

## 1. 🔠 Bitwise Operators

| Operator | Description             | C++ Syntax | Python Syntax |
|----------|--------------------------|------------|---------------|
| `&`      | Bitwise AND              | `a & b`    | `a & b`       |
| `|`      | Bitwise OR               | `a | b`    | `a | b`       |
| `^`      | Bitwise XOR              | `a ^ b`    | `a ^ b`       |
| `~`      | Bitwise NOT              | `~a`       | `~a`          |
| `<<`     | Left Shift               | `a << n`   | `a << n`      |
| `>>`     | Right Shift              | `a >> n`   | `a >> n`      |

---

## 2. 🧰 Binary Representations and Number Systems

- Computers store numbers in **binary**.
- Negative numbers are typically stored in **two's complement**.
- Python supports arbitrary-length integers. C++ uses fixed-width (int = 32 bits).
- Important to understand signed vs unsigned behavior in C++.

```cpp
int a = -5;
bitset<32> b(a); // displays two's complement in binary
```

```python
bin(-5 & 0xffffffff) # masks 32-bit representation
```

---

## 3. 🔧 Common Bit Manipulation Techniques

### Check if a bit is set:
```cpp
bool isSet = (num & (1 << i)) != 0;
```
```python
is_set = (num & (1 << i)) != 0
```

### Set a bit:
```cpp
num |= (1 << i);
```
```python
num |= (1 << i)
```

### Clear a bit:
```cpp
num &= ~(1 << i);
```
```python
num &= ~(1 << i)
```

### Toggle a bit:
```cpp
num ^= (1 << i);
```
```python
num ^= (1 << i)
```

### Count set bits (Kernighan's algorithm):
```cpp
int count = 0;
while (n) {
    n &= (n - 1);
    count++;
}
```
```python
count = 0
while n:
    n &= (n - 1)
    count += 1
```

### Power of Two Check:
```cpp
bool isPowerOfTwo = (n > 0 && (n & (n - 1)) == 0);
```
```python
is_power = n > 0 and (n & (n - 1)) == 0
```

### Rightmost Set Bit:
```cpp
int rightmost = n & -n;
```
```python
rightmost = n & -n
```

---

## 4. 🚀 Advanced Bit Tricks and Patterns

### Swap two numbers (no temp):
```cpp
a ^= b;
b ^= a;
a ^= b;
```
```python
a ^= b
b ^= a
a ^= b
```

### XOR from 1 to n:
```cpp
int xorToN(int n) {
    int mod = n % 4;
    return (mod == 0) ? n : (mod == 1) ? 1 : (mod == 2) ? n + 1 : 0;
}
```
```python
def xor_to_n(n):
    return [n, 1, n + 1, 0][n % 4]
```

### Find single element (others are twice):
```cpp
int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int num : nums) res ^= num;
    return res;
}
```
```python
def single_number(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
```

### Find two unique numbers:
```cpp
// XOR all -> get xor of two unique numbers
int xorAll = 0;
for (int x : arr) xorAll ^= x;
int mask = xorAll & -xorAll; // rightmost set bit
int a = 0, b = 0;
for (int x : arr) {
    if (x & mask) a ^= x;
    else b ^= x;
}
```

---

## 5. 🔄 Real-world DSA Applications

- **Subsets/Combinations**: Using bitmasks
- **Graph Coloring**: Valid states as bitmasks
- **DP with States**: `dp[mask][i]` format for TSP, etc.
- **Trie Compression**: Flags, tries with bitwise ops
- **Integer Manipulation**: Count 1s, reverse bits

---

## 6. 🔹 Bitmasking and Subset Enumeration

### All subsets:
```cpp
void generateSubsets(vector<int>& arr) {
    int n = arr.size();
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++)
            if (mask & (1 << i)) subset.push_back(arr[i]);
        // process subset
    }
}
```
```python
def generate_subsets(arr):
    n = len(arr)
    for mask in range(1 << n):
        subset = [arr[i] for i in range(n) if mask & (1 << i)]
        # process subset
```

---

## 7. 📊 Bit Manipulation Problems for Practice

| Problem Name                     | Platform     |
|----------------------------------|--------------|
| Single Number (136)              | Leetcode     |
| Number of 1 Bits (191)           | Leetcode     |
| Reverse Bits (190)               | Leetcode     |
| Bitwise AND of Range (201)       | Leetcode     |
| Maximum XOR of Two Numbers       | Leetcode     |
| Counting Bits (338)              | Leetcode     |
| Subsets using Bitmask            | Custom       |
| Power of Two (231)               | Leetcode     |
| Two Single Numbers (260)         | Leetcode     |
| Count Set Bits                   | GeeksForGeeks|

---

## 🚀 Final Notes

- Use `bitset` in C++ for visual debugging.
- Practice XOR-based patterns.
- Master Kernighan's trick.
- Explore Bitmask DP and Graph Bitmasking.

With a strong grip on bitwise techniques, you can ace many low-level optimization problems in interviews.

---

