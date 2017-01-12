import Queue
# import Queue, q = Queue.PriorityQueue()  
# q.put((a tuple))     q.qsize()   q.get()

class Solution:
    def frequencysrot(self, lst):
        dict = {}
        q = Queue.PriorityQueue()
        for str in lst:
            if str in dict:
                dict[str] += 1
            else:
                dict[str] = 1

        for key,value in dict.iteritems():
            #use tuple here
            #Priority queue will sort first parameter
            q.put((value,key))

        for i in xrange(q.qsize()):
            print q.get()


if __name__ == '__main__':
    lst = ['33','33','33','33','444','444','1']
    Solution().frequencysrot(lst)