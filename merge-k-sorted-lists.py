#23
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        curr = dummy
        heap = []
        for node in lists:
            if node:
                heap.append((node.val,node))
        heapq.heapify(heap)
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return dummy.next
