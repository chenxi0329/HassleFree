#103
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return root
        queue = [root]
        result = []
        line = 0

        while queue:
            level = []
            size = len(queue)
            for i in xrange(size):
                node = queue.pop(0)
                if node:
                    if line % 2 == 0:
                        #append val here, if you append node, Python won't print details about your object
                        level.append(node.val)
                    else:
                        level.insert(0,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
            line += 1
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().zigzagLevelOrder(root)
    print result