class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        INF = 10**20
        options = deque()
        dp = [num for num in nums]
        for i in range(len(nums)-1,-1,-1):
            while options and options[-1]-i>k:
                options.pop()
            if options:
                dp[i]=max(dp[i],nums[i]+dp[options[-1]])
            while options and dp[i]>dp[options[0]]:
                options.popleft()
            options.appendleft(i)
        return max(dp)

