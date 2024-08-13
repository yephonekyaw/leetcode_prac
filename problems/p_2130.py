def pairSum(head):
    stack = []
    while head is not None:
        stack.append(head.val)
        head = head.next
    
    max_sum = -float('inf')
    l, r = 0, len(stack) - 1
    while l < r:
        local_sum = stack[l] + stack[right]
        if local_sum > max_sum:
            max_sum = local_sum
        l, r = l + 1, r + 1
    return max_sum