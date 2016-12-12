#338
class Solution(object):
    #a trivial approach
    def countBits0(self, num):
        if not num:
            return [0]
        #declare list with fixed size
        res=[0] * (num+1)
        
        # cuz index 0 has already been defined, so for loop start with 0
        for n in xrange(1, num+1):
                res[n] = list(bin(n)[2:]).count('1')
        return res
        
    #apporach wiht n&n-1
    def countBits(self, num):
        if not num:
            return [0]
            
        res = [0] * (num+1)
        
        #if u dont start with 1 here, it will fail following n&n-1 process
        for n in xrange(1,num+1):
            res[n] = res[n&(n-1)]+1
        return res
        
        
    #future reading
    #http://blog.csdn.net/liyuefeilong/article/details/51086001