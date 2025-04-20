#include <cctype>
#include <cmath>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
class Solution {
public:
  void printFreq(unordered_map<int, int> freq) {
    for (const auto pair : freq) {
      cout << pair.first << " " << pair.second << " ";
      cout << endl;
    }
  }
  int numRabbits(vector<int> &answers) {
    unordered_map<int, int> freq;
    for (const auto num : answers) {
      freq[num]++;
    }
    int total = 0;
    // printFreq(freq);
    for (const auto pair : freq) {
      total += ceil((double)pair.second / (pair.first + 1)) * (pair.first + 1);
    }
    return total;
  }
};
int main() {
  Solution sol;
  vector<int> arr = {1, 1, 2};
  int val = sol.numRabbits(arr);
  cout << val << endl;
}
