class Solution:
    def romanToInt(self, s: str) -> int:
        romanPairs = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        number = 0
        i = 0
        while i < len(s):
            l = s[i]
            subtracted = False
            if (l == "I") and i + 1 < len(s):
                if (s[i+1] == "V"):
                    number += 4
                    i += 2
                    subtracted = True
                elif (s[i+1] == "X"):
                    number += 9
                    i += 2
                    subtracted = True
            elif (l == "X") and i + 1 < len(s):
                if (s[i+1] == "L"):
                    number += 40
                    i += 2
                    subtracted = True
                elif (s[i+1] == "C"):
                    number += 90
                    i += 2
                    subtracted = True
            elif (l == "C") and i + 1 < len(s):
                if (s[i+1] == "D"):
                    number += 400
                    i += 2
                    subtracted = True
                elif (s[i+1] == "M"):
                    number += 900
                    i += 2
                    subtracted = True
            
            if not subtracted:
                number += romanPairs[l]
                i += 1
        
        return number
