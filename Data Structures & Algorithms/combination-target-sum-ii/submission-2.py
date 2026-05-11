class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(i, target, current):
            if target == 0:
                output.append(current)
                return
            if target < 0:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                backtrack(j + 1, target - candidates[j], current + [candidates[j]])
        output = []
        backtrack(0, target, [])
        return output