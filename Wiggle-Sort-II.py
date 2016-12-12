#324
#!!!!!!!need extra attetion on DP one
#天下武功 唯快不破

class Solution(object):
    
    #T: O(nlgn) S:O(n) 
    def wiggleSort0(self, nums):
        #nums.sort() change input list
        #sorted(nums) doesn't
        snums = sorted(nums)
        for i in xrange(1, len(nums), 2):
            #pop() returns most right
            #pop(0) returns most left
            nums[i] = snums.pop()
        for i in xrange(0, len(nums), 2):
            nums[i] = snums.pop()
            
    #T: O(N)
    #S: O(1)
    #quick select
    def wiggleSort(self,nums):
        mid = self.quickselect(nums, len(nums)/2)

        print "quick select: ", nums

        # mapping from index to wiggle index
        # example: [0, 1, 2, ... , n - 1, n] to [1, 3, 5, ... , 0, 2, 4, ...]
        N = len(nums)
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[(1 + 2*j)%(N|1)] > mid:
                nums[(1 + 2*i)%(N|1)], nums[(1 + 2*j)%(N|1)] = nums[(1 + 2*j)%(N|1)], nums[(1 + 2*i)%(N|1)]
                i+=1
                j+=1
            elif nums[(1 + 2*j)%(N|1)] < mid:
                nums[(1 + 2*j)%(N|1)], nums[(1 + 2*k)%(N|1)] =  nums[(1 + 2*k)%(N|1)], nums[(1 + 2*j)%(N|1)]
                k-=1
            else:
                j+=1
    
    def partition(self,array, pivotId, left, right):
        pivotValue = array[pivotId]
        array[right], array[pivotId] = array[pivotId], array[right]
    
        pos = left
        for j in range(left, right):
            if array[j] < pivotValue:
                array[pos], array[j] = array[j], array[pos]
                pos += 1
    
        array[right], array[pos] = array[pos], array[right]
        return pos

    def quickselect(self,array, id):
        #random.seed(time.time())
        return self.select(array, id, 0, len(array)-1)
    
    def select(self, array, id, left, right):
        while left < right:
            pivot = random.randrange(left, right)
    
            pivotPos = self.partition(array, pivot, left, right)
    
            if pivotPos == id:
                return array[pivotPos]
            elif pivotPos < id:
                left = pivotPos+1
            else:
                right = pivotPos-1
        return array[right]