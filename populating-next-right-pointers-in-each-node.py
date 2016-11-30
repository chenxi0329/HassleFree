#116
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left =None
        self.right = None
        self.next = None
    def __repr__(self):
        if not self:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    def connect(self, root):
        if not root:
            return root
        queue = [root]
        while queue:
            #previous records the node we previously visited
            previous = None
            size = len(queue)
            for i in xrange(size):
                curr = queue.pop(0)
                #first iteration for each row won't hit that if loop
                if previous:
                    # if we are not visiting most left node, then previous node should point to currnode
                    previous.next = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
             #record previous node for next iteration
                previous = curr
        
if __name__ == '__main__':
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left.left, root.left.right, root.right.left, root.right.right = TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
    Solution().connect(root)
    print root
    print root.left
    print root.left.left