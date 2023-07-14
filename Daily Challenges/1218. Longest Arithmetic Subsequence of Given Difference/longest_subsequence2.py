class Solution:
    def longestubsequence(self, arr: List[int], difference: int) -> int:
        dp = collections.defaultdict(int)
        for num in arr:
            prev = dp[num-difference]
            dp[num] = max(dp[num],prev+1)
        return max(dp.values())