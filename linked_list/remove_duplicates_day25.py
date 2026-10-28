def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr:
            # Check if current node has duplicates
            if curr.next and curr.val == curr.next.val:
                # Advance curr to the end of the duplicate run
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Skip all nodes in the duplicate run
                prev.next = curr.next
            else:
                # No duplicates, advance prev
                prev = prev.next
                
            curr = curr.next
            
        return dummy.next
