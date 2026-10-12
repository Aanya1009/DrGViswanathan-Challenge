def isPalindrome(self, head: ListNode | None) -> bool:
        result=[]
        current=head
        while current:
            result.append(current.val)
            current=current.next
        return result==result[::-1]