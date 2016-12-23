#15 3sum
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in xrange(len(nums)-2):
            if i == 0 or nums[i-1] < nums[i]:
                left, right = i+1, len(nums)-1
                while left < right:
                    if nums[left]+nums[right] == -nums[i]:
                        res.append([nums[i], nums[left], nums[right]])
                        left +=1;
                        right-=1;
                        #remove duplicates?
                        while left <right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                        
                    elif nums[left] + nums[right] < -nums[i]:
                        #move left pointer to right
                        while left < right:
                            left += 1
                            if nums[left-1] < nums[left]: break
                        
                    else:
                        #move right pointer to left
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right+1]:break                    
        return res