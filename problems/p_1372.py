def count_zig_zag(node, deep, prev_dir):
    if node is None:
        return deep - 1

    l_deep = self.count_zig_zag(node.left, deep + 1, "left") if prev_dir != "left" else self.count_zig_zag(node.left, 1, "left")
    r_deep = self.count_zig_zag(node.right, deep + 1, "right") if prev_dir != "right" else self.count_zig_zag(node.right, 1, "right")
    return max(l_deep, r_deep)
    
def longestZigZag(root):
    return self.count_zig_zag(root, 0, "")