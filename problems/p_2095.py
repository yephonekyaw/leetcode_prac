def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    tmp = head
    count = 0
    while tmp != None:
        count += 1
        tmp = tmp.next

    if count == 1:
        return None

    mid = math.floor(count / 2)
    i = 0
    tmp = head
    while i < mid - 1:
        tmp = tmp.next
        i += 1

    deleted_node = tmp.next
    tmp.next = deleted_node.next
    return head
