"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def add(current):
            if not current:
                return
            if hashMap.get(current, None):
                return hashMap.get(current)
            new_node = Node(current.val)
            hashMap[current] = new_node
            
            for neighbor in current.neighbors:
                new_neighbor = add(neighbor)
                if new_neighbor:
                    new_node.neighbors.append(new_neighbor)
            return new_node
        hashMap = dict()
        copy_graph = add(node)
        return copy_graph
