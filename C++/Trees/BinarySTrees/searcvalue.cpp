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
  TreeNode *searchBST(TreeNode *root, int val) { return dfs(root, val); }

private:
  TreeNode *dfs(TreeNode *root, int val) {
    if (root == nullptr)
      return nullptr;
    if (root->val == val)
      return root;

    else if (root->val > val && root->left != nullptr)
      dfs(root->left, val);
    else if (root->val < val && root->right && root->right != nullptr)
      return dfs(root->right, val);
  }
};
