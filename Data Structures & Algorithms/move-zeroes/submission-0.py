class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        for n in nums[:]:
            if n == 0:
                nums.remove(0)
                zero.append(0)
        nums += zero