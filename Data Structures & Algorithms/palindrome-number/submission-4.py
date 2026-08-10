class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        intString = str(abs(x))
        if len(intString) % 2 == 1:
            middleIndex = len(intString) // 2
            left = -1
            right = 1
            while (middleIndex + left) >= 0 and (middleIndex + right) < len(intString):
                if intString[middleIndex + left] != intString[middleIndex + right]:
                    return False
                else:
                    left -= 1
                    right += 1
            return True
        elif len(intString) % 2 == 0: 
            midLeft = int((len(intString) / 2) - 1)
            midRight = int((len(intString) / 2))
            while midLeft >= 0 and midRight < len(intString):
                if intString[midLeft] != intString[midRight]:
                    return False
                else:
                    midLeft -= 1
                    midRight += 1
            return True
        return False