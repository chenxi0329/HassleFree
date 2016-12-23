#20
class Solution(object):
    def isValid(self, s):
        dict = { ')':'(', ']':'[','}':'{'}
        left = ['(',  '[', '{']
        stack = []
        for i in xrange(len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif stack == [] or stack.pop() != dict[s[i]]:
                return False
        
        if stack:
            return False
        return True