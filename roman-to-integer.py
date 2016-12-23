#13
class Solution(object):
    def romanToInt(self, s):
        number = { 'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res = 0
        #way to revert list
        s = s[::-1]
        last = None
        for letter in s:
            if last and number[letter]<last:
                res -= 2* number[letter]
            res += number[letter]
            last = number[letter]
        return res