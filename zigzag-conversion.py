#6
class Solution(object):
    def convert(self, str, numRows):
        if numRows == 1:
            return str

        direction = -1                      #direction starts from -1 cuz 0 is border so  
                                            #direction will be changed after first run
        rows, idx = [""]*numRows, 0
        for char in str:
            rows[idx] += char
            if idx == 0 or idx == numRows-1: #change direction if it hits border
                direction = -direction       #build a great wall! 
            idx += direction                 # move index to next cell 
        return "".join(rows)

if __name__ == "__main__":
    print Solution().convert("PAYPALISHIRING", 1)
    print Solution().convert("PAYPALISHIRING", 4)
