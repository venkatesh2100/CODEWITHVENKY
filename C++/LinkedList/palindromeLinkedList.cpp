#include <bits/stdc++.h>
#include <stack>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
  bool isPalindrome(ListNode *head) {
    ListNode *mover = head;

    stack<int> st;

    while (mover != nullptr) {
      int val = mover->val;
      mover = mover->next;
      st.push(val);
    }

    ListNode *checker = head;
    while (checker != nullptr) {
      if (st.top() != checker->val) {
        return false;
      }
      st.pop();
      checker = checker->next;
    }

    return true;
  }
};
