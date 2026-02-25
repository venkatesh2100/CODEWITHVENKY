#include <bits/stdc++.h>
using namespace std;
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
  ListNode *mergeKLists(vector<ListNode *> &lists) {
    if (lists.empty()) {
      return nullptr;
    }

    while (lists.size() > 1) {
      vector<ListNode *> temp;
      for (int i = 0; i < lists.size(); i += 2) {
        ListNode *l1 = lists[0];
        ListNode *l2 = i + 1 < lists.size() ? ListNode[1] : nullptr;
        temp.push_back(mergeKLists(l1, l2));
      }
      lists = move(temp);
    }
    return lists[0];
  }

private:
  ListNode *mergeList(ListNode *l1, ListNode *l2) {
    ListNode head;
    ListNode *node = &head;

    while (l1 && l2) {
      if (l1->val > l2->val) {
        node->next = l2;
        l2 = l2->next;
      } else {
        node->next = l1;
        l1 = l1->next;
      }
    }

    node->next = l1->next ? l1 : l2;
    return head.next;
  }
};
