#2
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        isCarry = 0
        dummy = ListNode(-1)
        curr = dummy
        
        while l1 and l2:
            curr.next = ListNode((l1.val + l2.val + isCarry)%10)
            #cut whatever after .
            isCarry = (l1.val + l2.val + isCarry)/10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
            
        if l1:
            while l1:
                curr.next = ListNode((l1.val + isCarry)%10)
                isCarry = (l1.val + isCarry)/10
                l1 = l1.next    
                curr = curr.next    
        if l2:
            while l2:
                curr.next = ListNode((l2.val + isCarry)%10)
                isCarry = (l2.val + isCarry)/10
                l2 = l2.next    
                curr = curr.next    
            
        if isCarry is 1: curr.next = ListNode(1)
        return dummy.next