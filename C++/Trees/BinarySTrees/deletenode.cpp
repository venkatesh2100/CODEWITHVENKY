

#include <bits/stdc++.h>
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
  TreeNode *deleteNode(TreeNode *root, int key) {

    if (!root)
      return nullptr;
    TreeNode *part = nullptr;
    TreeNode *curr = root;

    while (curr && curr->val != key) {
      part = curr;
      if (curr->val > key)
        curr = curr->left;
      else
        curr = curr->right;
    }

    if (!curr)
      return root;
    // case 1: one or no child
    if (!curr->left || !curr->right) {
      TreeNode *child = curr->left ? curr->left : curr->right;
      // if key == root node.
      if (!part) {
        delete curr;
        return child;
      }

      if (part->left == curr) {
        part->left = child;
      } else {
        part->right = child;
      }

      // case 2: two childs
      delete curr;
    } else {
      TreeNode *succ = curr->right;
      TreeNode *succp = curr;

      while (succ->left) {
        succp = succ;
        succ = succ->left;
      }

      curr->val = succ->val;

      if (succp->left == succ) {
        succp->left = succ->right;
      } else {
        succ->right = succ->right;
      }
      delete succ;
    }

    return root;
  }
};
