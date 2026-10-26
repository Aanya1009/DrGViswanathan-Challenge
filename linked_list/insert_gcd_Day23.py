def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current=head
        while current.next:
            nxt=current.next
            gcd_val=math.gcd(current.val, nxt.val)
            current.next = ListNode(gcd_val, nxt)
            current=nxt
        return head
