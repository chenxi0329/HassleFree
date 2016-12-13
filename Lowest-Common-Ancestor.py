#236
#天下武功，唯快不破！！！

class Solution(object):
    #recursive approch
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root
        if root in (p,q):
            return root
        #recursive calls
        lc = self.lowestCommonAncestor(root.left, p, q)
        rc = self.lowestCommonAncestor(root.right, p, q)
        
        #LCA is neither p or q
        if lc and rc:
            return root
        else:
            if lc:
                return lc
            if rc:
                return rc
    #iterative way
    #todo
    #!!! do it in DFS way, non-recursive
    '''
    def lowestCommonAncestor0(self, root, p, q):
        pPath, qPath =[], []
        self.findPath(root,p, pPath)
        self.findPath(root,q, qPath)
        return findLCA(self,pPath,qPath)
        
    def findPath(self, root, target, path):
        if not root:
            return False
        path.append(root,key)
        if root.val is target.val:
            return True
        
        #search left, right sub tree
        if root.left is not None and self.findPath(root.left, path,target)
        or
        root.left is not None and self.findPath(root.left, path,target):
            return true
        path.pop()
        return False
    '''