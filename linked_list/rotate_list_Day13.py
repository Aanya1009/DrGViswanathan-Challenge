 def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        # 1. Get total length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # 2. Reduce k
        k = k % length
        if k == 0:
            return head

        # 3. Create a gap of k nodes between fast and slow
        fast = head
        for _ in range(k):
            fast = fast.next

        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 4. Re-link pointers
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head