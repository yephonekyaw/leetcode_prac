def reverse(self, cur, pre):
    if cur is None:
        return pre
    
    nex = cur.next
    cur.next = pre
    return self.reverse(nex, cur)

def reverseList(head):
    return self.reverse(head, None)