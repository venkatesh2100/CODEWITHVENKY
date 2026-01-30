#include <algorithm>
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
  int maxDepth(TreeNode *root) {

    if (root == nullptr) {
      return 0;
    }

    int maxleft = maxDepth(root->left);
    int maxright = maxDepth(root->right);

    return max(maxleft, maxright) + 1;
  }
};
