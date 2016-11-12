#LC26
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        lenNums = len(nums) 

        new, old = 0,1   
        while old<lenNums:
            if nums[new]!=nums[old]: 
                new += 1                
                nums[new] = nums[old] 
            old +=1        
        return new+1              

if __name__ == "__main__":
    print Solution().removeDuplicates([1,2,2,3])
    print Solution().removeDuplicates([1])
    print Solution().removeDuplicates([])