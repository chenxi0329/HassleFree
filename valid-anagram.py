#242
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == 0 and len(t) == 0:
            return True
        return sorted(s) == sorted(t)