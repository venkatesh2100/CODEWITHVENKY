# Strings Prep - DSA Memory

<details>
<summary>1. Reverse Words in a String (LeetCode 151)</summary>

### Current Implementation (Python)
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # s.split() handles multiple spaces and leading/trailing spaces automatically
        arr = s.split()
        res = ''

        for i in range(len(arr) - 1, -1, -1):
            res += arr[i]
            res += ' '

        # Remove the trailing space
        return res[:-1]
```

### Complexity Analysis
- **Time Complexity:** $O(N)$
  - `s.split()` takes $O(N)$ to scan the string.
  - The loop runs $W$ times (number of words), total concatenation $O(N)$.
- **Space Complexity:** $O(N)$
  - `arr` stores all words, requiring $O(N)$ space.
  - `res` stores the final string, requiring $O(N)$ space.

### C++ Reference
In C++, `std::stringstream` is the standard way to split by whitespace.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

class Solution {
public:
    std::string reverseWords(std::string s) {
        std::stringstream ss(s);
        std::string word;
        std::vector<std::string> words;

        // Split by whitespace
        while (ss >> word) {
            words.push_back(word);
        }

        std::string res = "";
        for (int i = (int)words.size() - 1; i >= 0; --i) {
            res += words[i];
            if (i > 0) res += " ";
        }
        return res;
    }
};
```

### Optimal Strategy & Refinements
1. **Pythonic One-Liner:** Use `" ".join(s.split()[::-1])`. This is idiomatic, faster, and guaranteed $O(N)$ as `join` pre-allocates memory.
2. **Interview Tip (In-place):** If an interviewer asks for $O(1)$ extra space (common in C++ where strings are mutable):
   - **Step 1:** Reverse the entire string.
   - **Step 2:** Reverse each individual word.
   - **Step 3:** Clean up extra spaces (leading, trailing, and multiple spaces between words) using a two-pointer approach.
3. **Edge Cases:** Multiple spaces between words, leading/trailing spaces, and empty strings. Both your Python `split()` and C++ `stringstream >>` handle these automatically.
</details>

<details>
<summary>2. Longest Common Prefix (LeetCode 14)</summary>

### Current Implementation (Python)
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Sorting is the key trick here.
        # It puts the most different strings at the first and last positions.
        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]
```

### Complexity Analysis
- **Time Complexity:** $O(N \cdot L \log N)$
  - $N$ is number of strings, $L$ is average length. Sorting takes $O(N \log N \cdot L)$.
- **Space Complexity:** $O(L)$ to store the result string.

### C++ Reference
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        if (strs.empty()) return "";
        std::sort(strs.begin(), strs.end());
        std::string first = strs[0], last = strs.back();
        int i = 0;
        while (i < first.length() && i < last.length() && first[i] == last[i]) i++;
        return first.substr(0, i);
    }
};
```

### Optimal Strategy & Refinements
1. **Vertical Scanning:** Better if the prefix is short or only in the first two strings.
2. **Horizontal Scanning:** Compare $S_1$ with $S_2$, then the result with $S_3$, etc.
3. **Sorting:** Lexicographical sorting makes $S_1$ and $S_n$ the most likely to differ, so we only need to compare those two.

</details>

---
