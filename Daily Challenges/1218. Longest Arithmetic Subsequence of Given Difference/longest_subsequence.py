class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        indexes = collections.defaultdict(list)
        for i,num in enumerate(arr):
            indexes[num].append(i)

        dp = [1]*len(arr)

        for i,num in enumerate(arr):
            prev_val = num-difference

            prev_index = bisect.bisect_right(indexes[prev_val],i)-1 if prev_val!=num else bisect.bisect_left(indexes[prev_val],i)-1
            if prev_index>-1:
                dp[i]=dp[indexes[prev_val][prev_index]]+1
        return max(dp)
