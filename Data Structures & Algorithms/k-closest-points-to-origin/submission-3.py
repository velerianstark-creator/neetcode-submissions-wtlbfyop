class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        hash_map = dict()
        for pos in range(len(points)):
            distance = points[pos][0]**2 + points[pos][1]**2
            if distance not in hash_map:
                distances.append(distance)
            hash_map.setdefault(distance, []).append(pos)
        distances.sort()
        output = []
        for closest in distances:
            for i in hash_map[closest]:
                output.append(points[i])
                if len(output) == k:
                    return output
