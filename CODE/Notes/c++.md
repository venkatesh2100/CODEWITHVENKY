
# 📌 C++ Notes for Competitive Programming (CP)

## 🚀 Introduction to C++
C++ is a **powerful, high-performance** programming language widely used in **competitive programming (CP)** due to its speed, STL (Standard Template Library), and fine-grained memory control.

## 🛠️ Basic Syntax & Setup
```cpp
#include <iostream>  // For input-output
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```
🔹 **`#include <iostream>`**: Includes standard input-output library.  
🔹 **`using namespace std;`**: Avoids writing `std::` before standard functions like `cout`.  
🔹 **`main()`**: Entry point of the program.  
🔹 **`cout` & `endl`**: Used for printing output.  

## 📌 Data Types & Variables
| Data Type | Description | Example |
|-----------|------------|---------|
| `int` | Integer (4 bytes) | `int x = 10;` |
| `float` | Floating point (4 bytes) | `float pi = 3.14;` |
| `double` | Double precision float (8 bytes) | `double d = 3.141592;` |
| `char` | Single character (1 byte) | `char c = 'A';` |
| `bool` | Boolean (true/false) | `bool flag = true;` |
| `string` | Sequence of characters | `string name = "Venky";` |
| `long long` | Large integer (8 bytes) | `long long bigNum = 1e18;` |

## 🔄 Control Flow
### ✅ If-Else
```cpp
if (x > 10) {
    cout << "Greater than 10";
} else {
    cout << "Less than or equal to 10";
}
```

### 🔄 Loops
#### ➡️ For Loop
```cpp
for (int i = 0; i < 5; i++) {
    cout << i << " ";
}
```
#### 🔄 While Loop
```cpp
int i = 0;
while (i < 5) {
    cout << i++ << " ";
}
```

## 📚 Functions
```cpp
int add(int a, int b) {
    return a + b;
}

int main() {
    cout << add(5, 3); // Output: 8
    return 0;
}
```

## 🗃️ Arrays & Vectors
### 📌 Arrays
```cpp
int arr[5] = {1, 2, 3, 4, 5};
cout << arr[2]; // Output: 3
```
### 📌 Vectors (Dynamic Arrays)
```cpp
#include <vector>
vector<int> v = {1, 2, 3};
v.push_back(4); // {1, 2, 3, 4}
v.pop_back();   // {1, 2, 3}
```

## 🔥 Strings & String Manipulation
```cpp
string s = "Hello";
s += " World"; // "Hello World"
cout << s.length(); // Output: 11
```

## 🔄 STL (Standard Template Library)
### ✅ Sorting
```cpp
#include <algorithm>
vector<int> v = {3, 1, 4, 1, 5};
sort(v.begin(), v.end());
```
### 🔍 Binary Search
```cpp
bool found = binary_search(v.begin(), v.end(), 3);
```

## 🔠 Maps & Sets
### 📌 Map (Key-Value Pairs)
```cpp
#include <map>
map<string, int> mp;
mp["Alice"] = 90;
mp["Bob"] = 85;
```
### 📌 Set (Unique Elements)
```cpp
#include <set>
set<int> s = {5, 3, 1, 4};
s.insert(2);
```

## 🔥 Recursion
```cpp
int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}
```

## 🔄 Dynamic Programming (DP)
```cpp
int dp[1001];
int fib(int n) {
    if (n <= 1) return n;
    if (dp[n] != -1) return dp[n];
    return dp[n] = fib(n - 1) + fib(n - 2);
}
```

## 🚀 Graphs (BFS & DFS)
### ✅ BFS (Breadth-First Search)
```cpp
#include <queue>
vector<int> adj[100];
bool visited[100];
void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                q.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }
}
```

### 🔥 DFS (Depth-First Search)
```cpp
void dfs(int node) {
    visited[node] = true;
    cout << node << " ";
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor);
        }
    }
}
```

## 🏁 Conclusion
C++ is an essential language for **competitive programming** due to its **fast execution**, **STL**, and **fine control over memory**. Keep practicing CP problems on **LeetCode, Codeforces, and AtCoder** to master it! 🚀🔥

