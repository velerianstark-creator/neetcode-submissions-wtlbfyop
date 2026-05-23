class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def spread(point, prev):
            if point in store:
                return False
            if point in visited and point != prev:
                return False
            connections = hash_edges.get(point, [])
            visited.add(point)
            for connection in connections:
                if connection == prev:
                    continue
                spread(connection, point)

            store.add(point)
            return True
        visited = set()
        hash_edges = dict()
        store = set()
        amount = 0
        for edge in edges:
            hash_edges.setdefault(edge[0], set()).add(edge[1])
            hash_edges.setdefault(edge[1], set()).add(edge[0]) 
        for point in range(n):
            if point not in store:
                amount += 1
            spread(point, -1)
        return amount