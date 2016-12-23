#1
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in xrange(len(nums)):
            curr = nums[i]
            # only check nums previous to curr index
            if target-curr in dict:
                # it is zero based now
                return (dict[target-curr], i)
            dict[curr] = i