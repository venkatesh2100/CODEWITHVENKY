#include <iostream>
#include <vector>
using namespace std;

// TODO: Implementation of Heaps ALGO.

int main() {
  vector<int> arr;
  for (int i = 0; i < 10; i++) {
    arr.push_back(i + 1);
  }

  for (const int &v : arr) {
    std::cout << v << endl;
  }
  std::cout << "Hello to Clangd" << endl;
}
