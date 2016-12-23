#12
class Solution(object):
    def intToRoman(self, num):
        # can use dict
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        letters = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        result = ''
        for i in xrange(0,len(values)):
            while num >= values[i]:
                num -= values[i]
                result += letters[i]
        return result