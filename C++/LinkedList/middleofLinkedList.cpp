#include <bits/stdc++.h>
#include <cstddef>
using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
  ListNode *middleNode(ListNode *head) {

    ListNode *rabbit = head;
    ListNode *turtle = head;

    while (rabbit != NULL && rabbit->next != NULL) {
      rabbit = rabbit->next->next;
      turtle = turtle->next;
    };

    return turtle;
  }
};
