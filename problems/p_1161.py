from collections import deque

def maxLevelSum(self, root):
    max_sum = -float('inf')
    max_lvl = None

    lvl = 1
    next_lvl = deque([root,])
    while next_lvl:
        cur_lvl = next_lvl
        local_sum = 0
        next_lvl = deque()
        while cur_lvl:
            node = cur_lvl.popleft()
            local_sum += node.val
            if node.left:
                next_lvl.append(node.left)
            if node.right:
                next_lvl.append(node.right)
        if local_sum > max_sum:
            max_sum = local_sum
            max_lvl = lvl
        lvl += 1
    
    return max_lvl