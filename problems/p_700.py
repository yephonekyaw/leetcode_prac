def searchBST(self, root, val):
    def search(node, val):
        if node is None:
            return None
        
        return node if node.val == val else \
               search(node.left, val) if val < node.val else \
               search(node.right, val)
    return search(root, val)