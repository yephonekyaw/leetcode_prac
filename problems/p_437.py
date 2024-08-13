def find_paths(node, runningSum, targetSum, prefix_sum):
    if node is None:
        return 0
    
    runningSum += node.val
    count = prefix_sum.get(runningSum - targetSum, 0)
    prefix_sum[runningSum] = prefix_sum.get(runningSum, 0) + 1
    count += self.find_paths(node.left, runningSum, targetSum, prefix_sum) + \
             self.find_paths(node.right, runningSum, targetSum, prefix_sum)
    prefix_sum[runningSum] -= 1
    return count

def pathSum(self, root, targetSum):
    prefix_sum = {0: 1}
    return self.find_paths(root, 0, targetSum, prefix_sum)