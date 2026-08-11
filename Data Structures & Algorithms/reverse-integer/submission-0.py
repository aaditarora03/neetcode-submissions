class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        t = ""
        if x < 0:
            t += "-"
            for i in range(len(s)-1, 0, -1):
                t += s[i]
        else:
            for i in range(len(s)-1, -1, -1):
                    t += s[i]
        if int(t) not in range((-2)**31, (2**31)-1):
            return 0
        return int(t)
        