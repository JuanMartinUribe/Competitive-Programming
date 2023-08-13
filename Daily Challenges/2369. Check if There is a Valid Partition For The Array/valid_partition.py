class Solution:
    def validPartition(self, nums: List[int]) -> bool: 
        
        dp = [False for _ in range(len(nums)+1)]
        dp[0] = True
        for i,num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                dp[i+1]|= dp[i-1]
            if i>1 and nums[i]==nums[i-1]==nums[i-2]:
                dp[i+1]|=dp[i-2]
            if i>1 and nums[i]==nums[i-1]+1==nums[i-2]+2:
                dp[i+1]|=dp[i-2]
            #print(dp)
        return dp[-1]
