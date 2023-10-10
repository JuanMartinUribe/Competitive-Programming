class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        nums = sorted(list(set(nums)))
        max_itvl = 0
        for i,num in enumerate(nums):
            r = bisect.bisect_left(nums,num+N)
            max_itvl = max(max_itvl,r-i) 
        return N-max_itvl
