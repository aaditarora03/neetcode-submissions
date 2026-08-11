class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while len(nums1) > m:
            nums1.pop()
        for val in nums2:
            nums1.append(val)
        nums1.sort()