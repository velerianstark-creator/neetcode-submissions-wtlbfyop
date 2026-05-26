class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        parent = [i for i in range(len(edges)+1)]
        for edge in edges:
            u, v = edge[0], edge[1]
            root_u = find(u)
            root_v = find(v)
            
            # Nếu chung gốc -> Việc thêm cạnh này sẽ tạo chu trình (vòng lặp)
            if root_u == root_v:
                return edge
                
            # Nếu khác gốc -> Gộp GỐC của nhóm này vào GỐC của nhóm kia
            parent[root_v] = root_u
        return []