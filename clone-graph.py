#133
#clone an undirected graph
class UndirectedGraphNode:
    def __init__(self,x):
        self.label = x
        self.neighbors = []   
    def setNeighbors(self, x):
        self.neighbors = x

class Solution:
    def cloneGraph(self,node):
        if not node:
            return None
        entryPoint = node
        #a dict which stores entries for 
        #old node --> new node
        dic = {}

        #create a new entry node for new graph
        copyNode = UndirectedGraphNode(node.label)

        #insert first  old node --> new node entry
        dic[node] = copyNode

        #use BFS to iterate all neighbors
        queue = [node]

        while queue:
            #pop(0) pops from left, pop() pops from right
            curr = queue.pop()

            #connect nodes or create new nodes based on curr
            for neighborNode in curr.neighbors:
                neighorNodeInNewGraph = None
                if neighborNode in dic:
                    neighorNodeInNewGraph = dic[neighborNode]
                else:
                    #if corresponding node not in new graph, we create it and add new entry to dic
                    newNode = UndirectedGraphNode(neighborNode.label)
                    dic[neighborNode] = newNode

                    neighorNodeInNewGraph = newNode
                    #because neighborNode is not in dic which means we haven't created corresponding node in new graph
                    # so throw it to queue and do the work
                    queue.append(neighborNode)
                    
                dic[curr].neighbors.append(neighorNodeInNewGraph)
                
        return dic[entryPoint]

if __name__ == '__main__':
    entry0 = UndirectedGraphNode(0)
    entry1 = UndirectedGraphNode(1)
    entry2 = UndirectedGraphNode(2)
    entry0.setNeighbors([entry1, entry2])
    entry1.setNeighbors([entry2])
    entry2.setNeighbors([entry2])
    res = Solution().cloneGraph(entry0)

    queue = [res]
    visited = []
    while queue:
        curr = queue.pop(0)
        visited.append(curr)
        print curr.label
        for node in curr.neighbors:
            if node not in visited:
                queue.append(node)

    print 'should expect 0122'