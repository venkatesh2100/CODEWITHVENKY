class Solution {
public:
  ListNode *oddEvenList(ListNode *head) {
    if (!head || !head->next)
      return head;

    ListNode dummy(0);
    ListNode *tail = &dummy;

    // odd nodes
    ListNode *odd = head;
    while (odd != nullptr) {
      tail->next = odd;
      tail = tail->next;

      if (odd->next == nullptr)
        break;
      odd = odd->next->next;
    }

    // even nodes
    ListNode *even = head->next;
    while (even != nullptr) {
      tail->next = even;
      tail = tail->next;

      if (even->next == nullptr)
        break;
      even = even->next->next;
    }

    tail->next = nullptr; // critical
    return dummy.next;
  }
};
