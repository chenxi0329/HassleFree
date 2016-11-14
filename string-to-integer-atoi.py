#LC 8
import sys
class Solution(object):
    def atoi(self, str):
        # pull max/min value for boundary checking usage
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        #striping input
        str = str.strip()
        if not str:
            return 0

        # make sure we take care of negative sign
        sign = -1 if str[0] =="-" else 1

        # get rid of + or - sign, if first digit contains non-number non +/- char
        # it will fail first loop and return
        if str[0] in ("+", "-"):
            str = str[1:]

        res, idx = 0, 0
        #only process numbers, if first digit is not number, directly return 0
        while idx<len(str) and str[idx].isdigit():
            #implment char to int by minusing unicode using ord method
            res = res*10+ ord(str[idx]) - ord ('0')
            idx += 1

        #prevent int overflow, make sure it return a int type
        res = sign * res
        res = min(MAX_INT,res)  #upper bound
        res = max(MIN_INT,res)  # lowe bound
        return res

if __name__ == "__main__":
    print Solution().atoi("") 
    print Solution().atoi("-1")
    print Solution().atoi("+1")
    print Solution().atoi("2147483647") 
    print Solution().atoi("2147483648") 
    print Solution().atoi("-2147483648")  
    print Solution().atoi("-2147483649")  
    print Solution().atoi(" b11228552307")  
