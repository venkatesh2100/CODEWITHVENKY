#include <bits/stdc++.h>
#include <string>
using namespace std;

string WordShorter(string word) {
  int n = word.length();
  if (n <= 10) {
    return word;
  }

  return string(1, word[0]) + to_string(n - 2) + word[n - 1];
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    string word;
    cin >> word;
    cout << WordShorter(word) << endl;
  }

  return 0;
}
