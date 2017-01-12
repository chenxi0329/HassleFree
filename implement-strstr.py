#28
class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack): return -1

        idx = 0
        while idx < len(haystack) - len(needle) +1:
            needlePt = 0
            hayPt = idx
            while needlePt < len(needle):
                # check if each character match
                if haystack[hayPt] == needle[needlePt]:
                    needlePt += 1
                    hayPt += 1
                else:
                    #non matching char, jump to check next char
                    break
            if needlePt == len(needle):
                break
            else:
                idx += 1
        if idx == len(haystack) - len(needle) +1:
            return -1
        return idx