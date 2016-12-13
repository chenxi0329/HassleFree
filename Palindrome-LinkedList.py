#234

class Solution(object):
    def isPalindrome(self, head):
        #input validation
        if head is None:
            return True
        
        #use fast slow pointer to find mid point
        fast, slow = head, head
        
            # how to use fast slow pointer approach
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half linkedlist
        curr, prev = slow.next,None
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        
        #compare value one by one
        p1, p2 = head, prev
        while p2 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        return p2 is None