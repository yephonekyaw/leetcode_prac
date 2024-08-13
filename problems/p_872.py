def seq_leaves(root):
    if root.left is None and root.right is None:
        return str(root.val) + " "
    
    if root is not None:
        return self.seq_leaves(root.left) + self.seq_leaves(root.right) 

def leafSimilar(root1, root2):
    return self.seq_leaves(root1) == self.seq_leaves(root2)