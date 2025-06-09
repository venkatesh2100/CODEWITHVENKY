from collections import deque
class TreeNode:
  def __init__(self,key) -> None:
    self.left = None
    self.right = None
    self.val = key


  ##preorder  function
  def preOrderTraversal(self,node):
    if not node:
      return None
    print(node.val," ")
    self.preOrderTraversal(node.left)
    self.preOrderTraversal(node.right)

  ##Post orderTraversal
  def postOrderTraversal(self,node):
    if not node:
      return None
    self.postOrderTraversal(node.left)
    self.postOrderTraversal(node.right)
    print(node.val ," ")

  def inOrderTraversal(self,node):
    if not node:
      return None
    self.inOrderTraversal(node.left)
    print(node.val, " ")
    self.inOrderTraversal(node.right)

  def BFS(self,node):
    if not node:
      return None
    q = deque([node])
    while q:
      curr = q.popleft()
      print(curr.val ," ")
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(20)
root.left.left = TreeNode(1)
root.right.right = TreeNode(30)

print("Pre Order Traverasl:: ROOT - LEFT - RIGHT")
root.preOrderTraversal(root)
print()

print("POST ORDER TRAVERSAL:: LEFT - RIGHT - ROOT")
root.postOrderTraversal(root)

print("INORDER TRAVSERSAL :: LEFT - ROOT - RIGHT")
root.inOrderTraversal(root)


print("BFS ::: LEVEL BY LEVEL")
root.BFS(root)