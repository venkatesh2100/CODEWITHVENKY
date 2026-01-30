#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
};

class Solution {
public:
  int dfs(TreeNode *node) {
    if (node == nullptr) {
      return 0;
    }

    int left = dfs(node->left);
    int right = dfs(node->right);
    int res = max(left + right, res);
    return max(left, right) + 1;
  }
  int diameterofTree(TreeNode *root) {
    int ans = dfs(root);
    return ans;
  }
};
