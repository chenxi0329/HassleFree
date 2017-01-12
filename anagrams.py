#49
class Solution(object):
    def groupAnagrams(self, strs):
        dict = {}
        res = []
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in dict:
                dict[sortedWord].append(word)
            else:
                dict[sortedWord]  = [word]

        for key in dict:
            res.append(dict[key])

        return res