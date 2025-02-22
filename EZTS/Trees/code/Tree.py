

class TreeNode:
  def __init__(self, value ,child=None):
    self.value = value
    self.child = child if child is not None else []

  def addChild(self, child):
    self.child.append(child)


root = TreeNode(10000)
root.addChild(100)
root.addChild(1002)
root.addChild(10020312)

print(root.child)
for child in root.child:
  print(child)
