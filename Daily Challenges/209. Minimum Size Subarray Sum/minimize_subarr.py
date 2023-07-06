class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        cur = 0
        ans = 10**20
        for i,num in enumerate(nums):
            cur+=num
            r = i
            while l<r and cur-nums[l]>=target:
                cur-=nums[l]
                l+=1
            if cur>=target:
                ans = min(ans,r-l+1)
        return ans if ans<10**20 else 0