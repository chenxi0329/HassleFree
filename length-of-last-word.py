class Solution:
    #58
    def lengthOfLastWord0(self, str):
        return len(str.strip().split(" ")[-1])

    def lengthOfLastWord1(self, str):
        length = 0
        str=str.strip()
        #how to reverse a String in Python way
        for char in reversed(str):
            if char != " ":
                length += 1
            else:
                break
        return length
if __name__ == "__main__":
    print Solution().lengthOfLastWord0("Ola Mi Amigo  ")
    print Solution().lengthOfLastWord1("  nong sha lei  ")
