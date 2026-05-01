# Bit Manipulation Prep - DSA Memory

## 💡 Quick Bit Tips
- **Check Odd/Even:** `(n & 1)` → `1` if odd, `0` if even.
- **Multiply by 2:** `n << 1`
- **Divide by 2:** `n >> 1`
- **Check if Power of 2:** `n > 0 && (n & (n - 1)) == 0`
- **Clear Lowest Set Bit:** `n & (n - 1)`
- **XOR Identity:** `x ^ x = 0` and `x ^ 0 = x`
- **Get i-th bit:** `(n >> i) & 1`

---

<details>
<summary>1. Check Odd or Even using Bits</summary>

### Current Implementation (Python)
```python
def isEven(n: int) -> bool:
    # If the last bit is 0, it's even. 
    # If the last bit is 1, it's odd.
    return (n & 1) == 0

def isOdd(n: int) -> bool:
    return (n & 1) == 1
```

### Complexity Analysis
- **Time Complexity:** $O(1)$
  - Bitwise operations are constant time operations.
- **Space Complexity:** $O(1)$

### C++ Reference
```cpp
#include <iostream>

class BitUtils {
public:
    static bool isEven(int n) {
        return (n & 1) == 0;
    }
    
    static bool isOdd(int n) {
        return (n & 1) != 0;
    }
};
```

### Optimal Strategy & Refinements
1. **Why Bits?** Bitwise `&` is generally faster than the modulo operator `%` at the hardware level, though modern compilers often optimize `n % 2` to `n & 1` automatically.
2. **Negative Numbers:** In Python, `n % 2` always returns a result with the same sign as the divisor (2), so `-1 % 2` is `1`. In C++, `-1 % 2` is `-1`. However, `n & 1` works consistently across most languages for checking the parity bit.
3. **Common Interview Follow-up:** "How do you count the number of set bits (1s)?" → Use `n & (n-1)` in a loop (Brian Kernighan’s Algorithm).

</details>

---
