#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> arr;
  for (int i = 0; i < 10; i++) {
    arr.push_back(i);
  }

  // print
  for (const auto &v : arr) {
    cout << v << "";
  }
  return 0;
}
