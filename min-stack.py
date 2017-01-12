#155
import sys
class MinStack(object):

    def __init__(self):
        self.lst = []
        self.minlst = []

    def push(self, x):
        self.lst.append(x)
        if len(self.minlst) == 0 or x < self.minlst[-1]:
            self.minlst.append(x)

    def pop(self):
        if len(self.lst) == 0:
            return
        tmp = self.lst.pop()
        if self.minlst[-1] == tmp:
            self.minlst.pop()

    def top(self):
        if len(self.lst) == 0:
            return
        return self.lst[-1]

    def getMin(self):
        if len(self.minlst) == 0:
            return
        return self.minlst[-1]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    print minStack.getMin();  # --> Returns -3.
    minStack.pop();
    print minStack.top();      #--> Returns 0.
    print minStack.getMin();   #--> Returns -2.