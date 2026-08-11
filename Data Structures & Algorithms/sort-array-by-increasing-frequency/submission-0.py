class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()

        var = {}
        arr = []

        frequency = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                frequency += 1
            else:
                # save the number we just finished counting
                var[nums[i - 1]] = frequency
                frequency = 1

        # save the final number
        var[nums[-1]] = frequency

        print(var)

        # increasing frequency
        # if frequency is equal, decreasing number
        sorted_data = sorted(
            var.items(),
            key=lambda item: (item[1], -item[0])
        )

        print(sorted_data)

        for key, value in sorted_data:
            x = 1

            while x <= value:
                arr.append(key)
                x += 1

        return arr