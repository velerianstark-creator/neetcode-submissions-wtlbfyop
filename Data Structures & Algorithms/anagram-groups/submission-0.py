class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        process = {}
        result =[]
        for text in strs:
            hash_text = {i: 0 for i in range(26)}
            hash_value = ""
            for ch in text:
                hash_text[ord(ch) - ord('a')] += 1
            for key in hash_text:
                if hash_text[key] != 0:
                    hash_value += chr(ord('a') + key) + str(hash_text[key])
            process.setdefault(hash_value, []).append(text)
        for value in process.values():
            result.append(value)
        return result
    
        


