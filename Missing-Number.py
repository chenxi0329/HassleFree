#268
class Solution(object):
    
    #use math
    def missingNumber0(self, nums):
        #calculate real sum
        #equation n*(n+1)/2
        sum = (len(nums)*(len(nums)+1))/2
        realSum = 0
        #calculate actual sum
        for num in nums:
            realSum += num
        return sum - realSum
    
    #real list xor actual list
    def missingNumber1(self, nums):
        res = 0
        for i in xrange(len(nums)):
            res ^= (i+1)^nums[i]
        return res
        
    #binary search
    def missingNumber(self, nums):
        nums.sort()
        left, right = 0, len(nums)
        while left < right:
            mid = (right-left)/2 + left
            if nums[mid] > mid:
                right = mid
            else:
                left = mid+1
            
        return right;
        