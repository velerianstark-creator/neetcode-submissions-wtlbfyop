class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        memo = {0, 1, 2}
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                for i in range(3):
                    if i in memo and triplet[i] == target[i]:
                        memo.remove(i)
                if not memo:
                    return True
        return False
