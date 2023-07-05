class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(0) == 0: return len(nums)-1
        zero_index = []
        for i,num in enumerate(nums):
            if num==0:
                zero_index.append(i)
        ans = 0
        for i,index in enumerate(zero_index):
            last_zero = -1 if i==0 else zero_index[i-1]
            next_zero = len(nums) if i==len(zero_index)-1 else zero_index[i+1]
            #print((index-last_zero-1),(next_zero-index-1))
            ans = max(ans,(index-last_zero-1)+(next_zero-index-1))
        return ans