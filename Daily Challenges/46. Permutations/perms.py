class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def perms(cur):
            if len(cur)==len(nums):
                return [cur]
            else:
                ans = []
                for num in nums:
                    if num not in cur:
                        ans+=perms(cur+[num])
                return ans
        return perms([])