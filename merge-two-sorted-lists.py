#21
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if None == l1: return l2
        if None == l2: return l1
        dummy = ListNode(-1)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
                
        if l1 == None: curr.next = l2
        else : curr.next = l1
        
        return dummy.next
        