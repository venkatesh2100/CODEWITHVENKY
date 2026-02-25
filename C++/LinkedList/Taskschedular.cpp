#include <bits/stdc++.h>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

struct ListNode {
  char val;
  ListNode *next;
  ListNode(char x) : val(x), next(nullptr) {}
};

class Solution {
public:
  ListNode *leastInterval(vector<char> &tasks, int n) {

    unordered_map<char, int> freq;
    for (char ch : tasks) {
      freq[ch]++;
    }

    // Max heap (frequency, task)
    priority_queue<pair<int, char>> pq;
    for (auto &p : freq) {
      pq.push({p.second, p.first});
    }

    ListNode dummy('#');
    ListNode *tail = &dummy;

    while (!pq.empty()) {

      int cycle = n + 1;
      vector<pair<int, char>> store;

      while (cycle > 0) {

        if (!pq.empty()) {
          auto [count, task] = pq.top();
          pq.pop();

          // Add task to linked list
          tail->next = new ListNode(task);
          tail = tail->next;

          if (count > 1) {
            store.push_back({count - 1, task});
          }
        } else {
          // Idle slot
          tail->next = new ListNode('#');
          tail = tail->next;
        }

        cycle--;

        if (pq.empty() && store.empty())
          break;
      }

      for (auto &p : store) {
        pq.push(p);
      }
    }

    return dummy.next;
  }
};
int main() {
  vector<char> tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
  int n = 2;

  Solution sol;
  ListNode *head = sol.leastInterval(tasks, n);

  // Print linked list
  while (head) {
    cout << head->val;
    if (head->next)
      cout << " -> ";
    head = head->next;
  }

  return 0;
}
