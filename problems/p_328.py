import math

def oddEvenList(head):
    count = 0
    tmp = head
    while tmp != None:
        tmp = tmp.next
        count += 1

    if count == 0 or count == 1 or count == 2:
        return head

    odd_count, even_count = math.ceil(count / 2), math.floor(count / 2)
    odd, even, even_head, i = head, head.next, head.next, 0
    while i < max(odd_count, even_count):
        if i < odd_count:
            odd.next = odd.next.next if odd.next != None else None
            odd = odd.next if odd.next != None else odd
        if i < even_count:
            even.next = even.next.next if even.next != None else None
            even = even.next if even.next != None else even
        i += 1
    
    odd.next = even_head
    return head


