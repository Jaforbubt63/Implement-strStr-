class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def hash_function(s):
            code = 0
            for c in s:
                code += ord(c)
            return code
        
        len_h = len(haystack)
        len_n = len(needle)
        
        if len_n == 0:
            return 0
        
        hash_code_needle = hash_function(needle)
        hash_code_rolling = hash_function(haystack[:len_n])
        
        if hash_code_needle == hash_code_rolling:
            if needle == haystack[:len_n]:
                return 0
            
            for i in range(1, len_h - len_n + 1):
                hash_code_rolling -= ord(haystack[i-1])
                hash_code_rolling += ord(haystack[i+len_n-1])
                if hash_code_needle == hash_code_rolling:
                    if haystack[i:i+len_n] == needle:
                        return i
                    
            return -1
        
        
        