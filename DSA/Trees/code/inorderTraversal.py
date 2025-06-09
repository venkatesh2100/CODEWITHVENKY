
def InorderTraversal(node):
    if not node:
        return None
    
    res = [] 
    stack = []

    while True:
        if node:
            stack.append(node)
            node = node.left 
        else:
            if not stack:
                break
            curr = stack.pop()
            res.append(curr.val)
            node = node.right 
    return res
