class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def checkValid(point, prev):
            if point in store:
                return True
            if point in visited and point != prev:
                return False
            
            connections = hash_edges.get(point, [])

            visited.add(point)
            for connection in connections:
                if connection == prev:
                    continue
                if not checkValid(connection, point):
                    return False
            store.add(point)
            return True
        visited = set()
        hash_edges = dict()
        store = set()
        if len(edges) != n -1:
            return False
        for edge in edges:
            hash_edges.setdefault(edge[0], set()).add(edge[1])
            hash_edges.setdefault(edge[1], set()).add(edge[0])
        
        for point in range(n):
            if not checkValid(point, -1):
                return False
        return True