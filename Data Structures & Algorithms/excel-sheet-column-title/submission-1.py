class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = ""
        while columnNumber > 0:
            columnNumber -= 1
            addition = columnNumber % 26
            letter = chr(65 + addition)
            column = letter + column
            columnNumber //= 26
        return column