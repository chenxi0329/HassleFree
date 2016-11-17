#LC 111
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #BFS approach
    def minDepth0(self, root):
        #input handle
        if root == None:
            return 0

        #initialize vars
        level = 1
        queue = [root]

        #start BFS
        while queue:
            for i in xrange(len(queue)):
                #FIFO queue, pop from most left AKA earliest element
                currNode = queue.pop(0)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                if currNode.left == None and currNode.right == None:
                    return level
            level += 1
        return level
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    print Solution().minDepth0(root)