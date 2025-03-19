#include <algorithm>
#include <chrono>
#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

using namespace std::chrono;

int add(int a, int b) { return a + b; }
int outArrays(vector<int> nums) {
  for (int i = 0; i < nums.size(); i++) {
    cout << nums[i] << endl;
  }
  return 0;
}
int outSet(set<int> nums) {
  for (int num : nums) {
    cout << num << endl;
  }
  return 0;
}

int main() {
  // Measure Time chrono...>
  auto start = high_resolution_clock::now();
  vector<int> arr = {10, 30, 40};

  arr.push_back(50);
  arr.pop_back();

  arr.push_back(1000);

  for (int i = 0; i < arr.size(); i++) {
    cout << arr[i] << endl;
  }

  cout << "Hello world" << endl;
  int x = pow(10, 2);

  if (x > 10) {
    cout << "X is Greater than 10";
  } else {
    cout << "X is Less than 10" << endl;
  }

  while (x < 0) {
    cout << x << endl;
    x -= 1;
  }
  cout << add(10, 30) << endl;

  // strings
  string s = "Venky";
  s += " Goodman";
  cout << s << endl;

  // sorting
  vector<int> nums = {10, 30, 1, 3, 5, 69};
  sort(nums.begin(), nums.end() - 3);
  outArrays(nums);

  // binary search
  bool found = binary_search(nums.begin(), nums.end(), 10);
  cout << found << endl;

  // sets
  set<int> snum = {100, 30, 100, 30};
  snum.insert(10);
  outSet(snum);

  auto end = high_resolution_clock::now(); // End time
  auto duration = duration_cast<milliseconds>(end - start);
  cout << "Execution Time: " << duration.count() << " ms" << endl;

  return 0;
}
