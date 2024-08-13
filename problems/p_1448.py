def count_goodNodes(root, path_max):
    if root is None:
        return 0
    
    return (1 if root.val >= path_max else 0) + self.count_goodNodes(root.left, max(path_max, root.val)) + self.count_goodNodes(root.right, max(path_max, root.val))

def goodNodes(root):
    return 1 + self.count_goodNodes(root, root.val)