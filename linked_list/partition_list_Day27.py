def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less_helper=ListNode(0)
        greater_helper=ListNode(0)
        less=less_helper
        greater=greater_helper
        current=head
        while current:
            if current.val<x:
                less.next=current
                less=less.next
            else:
                greater.next=current
                greater=greater.next
            current=current.next
        greater.next=None
        less.next=greater_helper.next
        return less_helper.next