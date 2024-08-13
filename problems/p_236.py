# def find_lca(node, p, q, lca):
    # if node is None:
    #     return False

    # lf = find_lca(node.left, p, q, lca)
    # rf = find_lca(node.right, p, q, lca)
    # itself = True if node.val == p.val or node.val == q.val else False
    # if lf and rf or lf and itself or rf and itself:
    #     lca[0] = node.val

    # return lf or rf or itself

def find_lca(self, node, p, q):
    if node is None or node == p or node == q:
        return node

    lf = self.find_lca(node.left, p, q)
    rf = self.find_lca(node.right, p, q)
    if lf and rf:
        return node
    else:
        return lf or rf

def lowestCommonAncestor(root, p, q):
    return self.find_lca(root, p, q)
