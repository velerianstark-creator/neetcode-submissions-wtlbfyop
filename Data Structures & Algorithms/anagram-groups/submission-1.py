class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        process = {}
        for text in strs:
            count = [0] * 26
            # hash_value = ""
            for ch in text:
                count[ord(ch) - ord('a')] += 1
            process.setdefault(tuple(count), []).append(text)
        return list(process.values())
    
        


