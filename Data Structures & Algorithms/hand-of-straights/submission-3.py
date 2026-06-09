class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        memo = {}
        for num in hand:
            memo[num] = memo.get(num, 0) + 1

        unique_keys = sorted(memo.keys())

        for key in unique_keys:
            if memo[key] > 0:
                count = memo[key]
            
                for i in range(key, key + groupSize):
                    if i not in memo or memo[i] < count:
                        return False
                    memo[i] -= count
                    
        return True