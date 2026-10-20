def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    current=head
    lst=[]
    while current:
        lst.append(current)
        current=current.next
    lst[k-1],lst[-k]=lst[-k],lst[k-1]

    head=lst[0]
    ll=head
    for val in lst[1:]:
        ll.next=val
        ll=ll.next
    ll.next=None
    return head