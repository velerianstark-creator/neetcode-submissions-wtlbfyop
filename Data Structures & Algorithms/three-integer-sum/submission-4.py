class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = []
        nums.sort(reverse=True)
        for num in nums:
            counter.append(0 - num)
        res = set()

        for k in range(1, len(nums) - 1):
            i = 0
            j = len(nums) - 1
            check_inf = []
            while (i < k and k < j):
                if len(check_inf) < 2:
                    check_inf.append([i, j])
                elif check_inf[0] == [i, j]:
                    break
                else:
                    check_inf.pop(0)
                    check_inf.append([i, j])
                if nums[i] + nums[j] > counter[k]:
                    i += 1
                    continue
                elif nums[i] + nums[j] < counter[k]:
                    j -= 1
                    continue
                else:
                    res.add(tuple([nums[i], nums[k], nums[j]]))
                    if k - i >= 1:
                        i += 1
                    elif k - j >= 1:
                        j -= 1
                    else: break

        return [list(result) for result in res]        