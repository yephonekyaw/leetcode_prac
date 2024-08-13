def rightSideView(self, root):
    lst = {}
    def right_view(node, lvl):
        if node is None:
            return

        if lst.get(lvl) == None:
            lst[lvl] = lst.get(lvl, [node.val])
        right_view(node.right, lvl + 1)
        right_view(node.left, lvl + 1)
    right_view(root, 0)
    print(lst)
    