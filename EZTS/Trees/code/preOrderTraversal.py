class TreeNode:
  def __init__(self,value ,child=None) -> None:
    self.value = value
    self.child = child if child is not None else []

  def addChild(self, child):
    self.child.append(child)
def PreOrderTraversal(root):
  if not root:
    return None

  print(root.value)
  for child in root.child:
    PreOrderTraversal(child)



root = TreeNode(50)
# print(root.child)
root.addChild(TreeNode(10))
root2 = TreeNode(160)
root.addChild(root2)
root2.addChild(TreeNode(200))
PreOrderTraversal(root)