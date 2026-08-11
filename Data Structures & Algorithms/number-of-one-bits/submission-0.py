class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        count = 0
        for i in range(2, len(s)):
            if s[i] == "1":
                count +=1
        return count