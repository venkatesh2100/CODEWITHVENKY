#include <iostream>
#include <queue>
using namespace std;

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int key) {
        val = key;
        left = nullptr;
        right = nullptr;
    }

    // Preorder Traversal (Root -> Left -> Right)
    void preOrderTraversal(TreeNode* node) {
        if (!node) return;
        cout << node->val << " ";
        preOrderTraversal(node->left);
        preOrderTraversal(node->right);
    }

    // Postorder Traversal (Left -> Right -> Root)
    void postOrderTraversal(TreeNode* node) {
        if (!node) return;
        postOrderTraversal(node->left);
        postOrderTraversal(node->right);
        cout << node->val << " ";
    }

    // Inorder Traversal (Left -> Root -> Right)
    void inOrderTraversal(TreeNode* node) {
        if (!node) return;
        inOrderTraversal(node->left);
        cout << node->val << " ";
        inOrderTraversal(node->right);
    }

    // BFS / Level Order Traversal
    void BFS(TreeNode* node) {
        if (!node) return;

        queue<TreeNode*> q;
        q.push(node);

        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();
            cout << current->val << " ";

            if (current->left) q.push(current->left);
            if (current->right) q.push(current->right);
        }
    }
};

int main() {
    // Creating the tree
    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(2);
    root->right = new TreeNode(20);
    root->left->left = new TreeNode(1);
    root->right->right = new TreeNode(30);

    cout << "Preorder Traversal (ROOT - LEFT - RIGHT): ";
    root->preOrderTraversal(root);
    cout << endl;

    cout << "Postorder Traversal (LEFT - RIGHT - ROOT): ";
    root->postOrderTraversal(root);
    cout << endl;

    cout << "Inorder Traversal (LEFT - ROOT - RIGHT): ";
    root->inOrderTraversal(root);
    cout << endl;

    cout << "BFS / Level Order Traversal: ";
    root->BFS(root);
    cout << endl;

    return 0;
}
  