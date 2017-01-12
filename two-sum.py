#1
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in xrange(len(nums)):
            curr = nums[i]
            if target - curr in dict:
                return (dict[target-curr],i)
            else:
                dict[curr] = i