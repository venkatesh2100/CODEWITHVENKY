

def PreOrderTraversal(node):
    if not node:
        return None
    res = []
    stack = [node]
    while stack:
        curr = stack.pop()
        # print(curr.val,' ' ,end=' ')
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res
