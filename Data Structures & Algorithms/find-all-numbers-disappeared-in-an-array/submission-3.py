class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        original_n = len(nums)
        missing = []
        if not nums:
            return []
        nums = list(set(nums))
        nums.sort()
        
        # Check gaps before the first element
        for j in range(1, nums[0]):
            missing.append(j)
            
        # Check gaps between elements
        for i in range(1, len(nums)):
            for j in range(nums[i-1]+1, nums[i]):
                missing.append(j)
        
        # Check gaps after the last element up to n
        n = original_n
        for j in range(nums[-1] + 1, n + 1):
            missing.append(j)
            
        return missing