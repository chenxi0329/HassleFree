#232
class Queue(object):
    def __init__(self):
        self.data = []
        

    def push(self, x):
        self.data.append(x)
        

    def pop(self):
        if len(self.data) == 0:
            return None
        currVal = self.data[0]
        #way to remove element from list
        self.data.remove(currVal)
        return currVal
        

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[0]
        

    def empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        