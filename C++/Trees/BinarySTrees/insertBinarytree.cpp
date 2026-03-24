
#include <bits/stdc++.h>
#include <cstddef>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
public:
  TreeNode *insertIntoBST(TreeNode *root, int val) {
    if (!root)
      return nullptr;

    TreeNode *curr = root;

    while (true) {
      if (curr->val > val) {
        if (!curr->left) {
          curr->left = new TreeNode(val);
          break;
        }
        curr = curr->left;
      } else {
        if (!curr->right)
          curr->right = new TreeNode(val);
        break;
      }
    }
    return root;
  };
};
