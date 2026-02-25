#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
  int w;

  int count = 0;
  cin >> w;
  while (w--) {
    int sum = 0;
    for (int i = 0; i < 3; i++) {
      int a;
      cin >> a;
      sum += a;
    }
    if (sum >= 2) {
      count += 1;
    }
  }
  cout << count;
  return 0;
}
