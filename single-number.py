import operator
#136
class Solution:
    def singleNumber0(self,nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key,value in count.items():
            if value == 1:
                return key

    def singleNumber1(self,nums):
        return reduce(lambda key,value:key^value, nums)

    def singleNumber2(self, nums):
        return reduce(operator.xor, nums)

if __name__ == '__main__':
    print Solution().singleNumber0([1, 1, 2, 2, 3])
    print Solution().singleNumber1([1, 1, 2, 2, 3])
    print Solution().singleNumber2([1, 1, 2, 2, 3])
