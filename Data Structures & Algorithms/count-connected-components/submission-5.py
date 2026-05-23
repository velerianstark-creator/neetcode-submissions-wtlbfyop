class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def spread(point):
            if point in visited:
                return False
            connections = hash_edges.get(point, [])
            visited.add(point)
            for connection in connections:
                spread(connection)
            return True
        visited = set()
        hash_edges = dict()
        amount = 0
        for edge in edges:
            hash_edges.setdefault(edge[0], set()).add(edge[1])
            hash_edges.setdefault(edge[1], set()).add(edge[0]) 
        for point in range(n):
            if point not in visited:
                amount += 1
            spread(point)
        return amount