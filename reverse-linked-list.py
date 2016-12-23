#206
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # Iterative solution.

    def reverseList(self, head):
        # a guard node which points to head node
        dummy = ListNode(-1)

        curr = head

        while curr:
            dummy.next, curr.next, curr = curr, dummy.next, curr.next
        
        #return head node
        return dummy.next

        
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reverseList(head)