class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            new_prefix = ""
            while i < len(s) and i < len(prefix):
                if s[i] == prefix[i]:
                    new_prefix += s[i]
                    i += 1
                else:
                    break
            prefix = new_prefix
            if not prefix: break
                    
        
        return prefix