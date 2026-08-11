class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        x = nums[0]

        nums.sort()
        for n in range(1, len(nums)):
            if nums[n] == nums[n-1]:
                count += 1
            else:
                count = 0
            if maxCount < count:
                maxCount = count
                x = nums[n]
        return x
