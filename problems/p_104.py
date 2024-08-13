def maxDepth(root):
    if root is None:
        return 0
    
    return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
