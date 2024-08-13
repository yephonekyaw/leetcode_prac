def reverseEachGroup(cur_node, prev_tail, k, og_head):
    k -= 1
    if cur_node == None and k >= 0:
        return [None, None]
    
    if k == 0:
        if prev_tail == None:
            og_head[0] = cur_node #this end node will become the head of ith group
        else:
            prev_tail.next = cur_node #this end node will become the head of ith group
        next_head = cur_node.next
        cur_node.next = None
        return [cur_node, next_head]
    
    returned, next_head = reverseEachGroup(cur_node.next, prev_tail, k, og_head)
    if returned == None and next_head == None:
        return [None, None]
    returned.next = cur_node
    cur_node.next = None
    return[cur_node, next_head]

def reverseKGroup(head, k):
    '''
        conditions:
        1. last group does not have k elements
        2. input can be divided into n groups of k elements
    '''
    prev_tail = None
    cur_head = head
    head = [None]
    while cur_head != None:
        prev_tail, next_head = reverseEachGroup(cur_head, prev_tail, k, head)
        if prev_tail == None and next_head == None:
            break
        prev_tail.next = next_head
        cur_head = next_head
    return og_head[0]
    