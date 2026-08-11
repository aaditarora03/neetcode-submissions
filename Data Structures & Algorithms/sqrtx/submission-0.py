class Solution:
    def mySqrt(self, x: int) -> int:
        i = x // 2
        while i * i != x:
            if i * i > x:
                i //= 2
            if i * i < x:
                i += 1
                if i * i > x:
                    return i-1
        return i