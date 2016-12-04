#LC26
#return len(new array)
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        #indexs for new/old sub lists
        ##new starts from 0
        ##old starts from 1
        new, old = 0,1   

        #while valid old index
        while old<len(nums):
            #if not a duplicated array
            ##olnly deal ineqaul case
            if nums[new]!=nums[old]: 
                #adjust new list entry point before moving element
                new += 1                

                #move element from old list to new list
                nums[new] = nums[old] 

            ## process next element from old 
            old +=1        

        #old stores index for last old value
        #+1 will return how many old elements get moved
        return new+1
        
if __name__ == "__main__":
    print Solution().removeDuplicates([1,2,2,3,4,5,5,6])
    print Solution().removeDuplicates([1])
    print Solution().removeDuplicates([])