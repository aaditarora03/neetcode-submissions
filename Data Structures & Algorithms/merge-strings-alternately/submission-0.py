class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        maxValue = max(len(word1), len(word2))
        for x in range(maxValue):
            if x < len(word1):
                s += word1[x]
            if x < len(word2):
                s += word2[x]
        return s