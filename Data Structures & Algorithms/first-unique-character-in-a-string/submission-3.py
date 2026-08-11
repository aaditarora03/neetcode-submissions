class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        repeat = True
        letters = set()
        while repeat:
            for i in range(len(s)):
                # print("i is currently", i)
                if i == (len(s) - 1):
                    if s[i] in letters:
                        return -1
                    else:
                        return i
                # print("s is", s)
                # print("checking if", s[i], "is in", letters)
                if s[i] in letters:
                    # print(s[i], "is in", letters)
                    # print("increasing i by 1")
                    i += 1
                    continue
                letters.add(s[i])
                # print("letters:", letters)
                # print("checking if" , s[i], "is in", s[i+1:])
                if s[i] not in s[i+1:]:
                    # print(s[i], "is not in", s[i+1:])
                    repeat = False
                    return i
                else:
                    # print(s[i], "IS in", s[i+1:])
                    # print("increasing i by 1 now")
                    # print("")
                    i += 1
        return -1