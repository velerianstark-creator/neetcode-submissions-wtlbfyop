class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [-float('inf')] * 3
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                for i in range(3):
                    current[i] = max(triplet[i], current[i])
                if current == target:
                    return True
        # if current == target:
        #     return True
        return False
