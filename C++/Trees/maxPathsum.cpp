#include <bits/stdc++.h>
#include <climits>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
};
class Solution {
public:
  int maxPathSum(TreeNode *root) {
    int sum = INT_MIN;
    dfs(root, sum);
    return sum;
  }

private:
  int dfs(TreeNode *root, int &sum) {

    if (!root)
      return 0;

    int ls = max(0, dfs(root->left, sum));
    int rs = max(0, dfs(root->right, sum));

    sum = max(sum, ls + rs + root->val);
    return root->val + ls + rs;
  }
};
