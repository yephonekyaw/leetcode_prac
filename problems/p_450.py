class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_node(node):
            prev, target = node, node
            while target and target.val != key:
                prev, target = target, target.left if key < target.val else target.right
            return prev, target

        parent, target = find_node(root)
        org_target = target

        # either the tree is empty or no target is found
        if parent == None or target == None:
            return root

        # the target does not have a right child
        if target.right == None:
            target = target.left
        # the target does not have a left child
        elif target.left == None:
            target = target.right
        else:
            tmp, replaced = target, target.right
            # find the feasible node to replace the deleted node in the right subtree
            while replaced.left:
                tmp, replaced = replaced, replaced.left

            # the immediate right child of the deleted node is the new parent
            if tmp == target:
                tmp.right = replaced.right
            else:
                tmp.left = replaced.right
            target.val = replaced.val

        if org_target == root:
            root = target
        elif org_target == parent.left:
            parent.left = target
        else:
            parent.right = target

        return root
