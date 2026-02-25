#include <bits/stdc++.h>
using namespace std;

vector<int> GreatestNext(vector<int> &nums) {
  int n = nums.size();
  vector<int> res(n, -1);
  stack<int> st;
  for (int i = 0; i < n; i++) {
    int val = nums[i];

    while (!st.empty() && nums[st.top()] < val) {
      res[st.top()] = val;
      st.pop();
    }
    st.push(i);
  }
  return res;
}

vector<int> SmallestNext(vector<int> &nums) {
  int n = nums.size();
  vector<int> res(n, -1);
  stack<int> st;
  for (int i = 0; i < n; i++) {
    int val = nums[i];

    while (!st.empty() && nums[st.top()] > val) {
      res[st.top()] = val;
      st.pop();
    }
    st.push(i);
  }
  return res;
}

vector<int> GreatestPrev(vector<int> &nums) {
  int n = nums.size();
  vector<int> res(n, -1);
  stack<int> st;
  for (int i = 0; i < n; i++) {
    int val = nums[i];

    while (!st.empty() && nums[st.top()] < val) {
      st.pop();
    }
    res[i] = st.empty() ? -1 : nums[st.top()];
    st.push(i);
  }
  return res;
}

vector<int> SmallestPrev(vector<int> &nums) {
  int n = nums.size();
  vector<int> res(n, -1);
  stack<int> st;
  for (int i = 0; i < n; i++) {
    int val = nums[i];

    while (!st.empty() && nums[st.top()] > val) {
      st.pop();
    }

    res[i] = st.empty() ? -1 : nums[st.top()];
    st.push(i);
  }
  return res;
}
int main() {
  vector<int> nums = {2, 1, 5, 3};
  vector<int> ans = GreatestNext(nums);

  for (int v : ans) {
    cout << v << " ";
  }
}
