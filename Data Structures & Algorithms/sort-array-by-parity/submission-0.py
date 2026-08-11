class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        if len(nums) == 1:
            return nums
        else:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] % 2 == 0:
                    even.append(nums[i])
                    nums.pop(i)
        even.sort()
        return even + nums
