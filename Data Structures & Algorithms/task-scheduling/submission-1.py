class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countMax= 0
        maxFreq = 0
        hash_map = dict()
        for task in tasks:
            hash_map[task] = hash_map.get(task, 0) + 1
        for count in hash_map.values():
            if count > countMax:
                countMax = count
                maxFreq = 1
            elif count == countMax:
                maxFreq += 1
        return max(len(tasks), (n+1) * (countMax - 1) + maxFreq)