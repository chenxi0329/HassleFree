#199
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #BFS
    def rightSideView(self,root):
        if not root:
            return root
        result,queue = [],[root]
        level = 0

        while queue:
            size = len(queue)
            for i in xrange(size):
                node = queue.pop(0)
                #compare with lengh of result, cuz we are adding from right,
                #whenever we go to a new level, most right element will always go to result
                if len(result) == level:
                    result.append(node.val)
                
                #push right first here
                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
            
            level += 1
        return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.right = TreeNode(9)
    root.right.left = TreeNode(20)
    root.right.right = TreeNode(15)
    root.right.right.right = TreeNode(16)
    root.right.right.right.right = TreeNode(17)
    print Solution().rightSideView(root)