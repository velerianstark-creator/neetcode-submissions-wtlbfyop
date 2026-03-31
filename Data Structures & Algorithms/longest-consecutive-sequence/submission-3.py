class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        convert_map = set()
        max = 1
        for num in nums:
            convert_map.add(num)
        
        for ele in convert_map:
            i = 1
            j = 1
            flag1 = True
            flag2 = True
            count = 1
            while(flag1 or flag2 == True):
                if flag1:
                    if (ele + i) in convert_map:
                        count += 1
                        i += 1
                    else:
                        flag1 = False
                if flag2:
                    if (ele - j) in convert_map:
                        count += 1
                        j += 1
                    else:
                        flag2 = False
            if count > max:
                max = count
        return max           
        