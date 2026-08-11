class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()

        count = 1
        result = -1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                # We just finished counting arr[i - 1]
                if count == arr[i - 1]:
                    result = arr[i - 1]

                count = 1

        # Check the last group
        if count == arr[-1]:
            result = arr[-1]

        return result