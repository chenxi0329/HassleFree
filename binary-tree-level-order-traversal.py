#102
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def levelOrder0(self, root):
        if root == None:
            return root
        #lists to store final result and queue
        res, queue = [], [root]
        #start BFS
        while queue:
            #tmp list to store level values 
            level = []
            for i in range (len(queue)):
                #pop happens inside of for loop
                currNode = queue.pop(0)
                #only add value in currNode
                level.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            #end of for loop means done with scanning current row
            res.append(level)
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print Solution().level(root)