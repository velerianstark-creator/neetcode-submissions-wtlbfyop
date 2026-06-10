class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        memo = set()
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                for i in range(3):
                    if triplet[i] == target[i]:
                        memo.add(i)
                if len(memo) == 3:
                    return True
        return False
