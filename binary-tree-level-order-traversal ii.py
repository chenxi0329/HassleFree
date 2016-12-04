#107
#return array in bottom up way
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #do it in BFS way by inserting to last position
    def levelOrderBottom0(self, root):
        if root == None:
            # don't return root here, root is None but program is looking for a list
            return []

        queue, res = [root], []

        while queue:
            level = []
            for i in xrange(len(queue)):
                currNode = queue.pop(0)
                level.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            #0 parameter first!!!
            res.insert(0,level)
        return res

    # use regular BFS and [::-1]
    def levelOrderBottom1(self, root):
        return Solution().levelOrder0(root)[::-1]

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
            res.append(level)
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print Solution().levelOrderBottom0(root)
    print Solution().levelOrderBottom1(root)