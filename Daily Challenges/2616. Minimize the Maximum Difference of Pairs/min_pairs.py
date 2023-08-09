class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0:
            return 0
        nums.sort()
        l = 0
        r = abs(nums[-1]-nums[0])
        def is_possible(diff):
            i = 0
            pairs = p
            while i<len(nums):
                if i >= len(nums)-1:
                    return False
                if abs(nums[i]-nums[i+1])<=diff:
                    i+=2
                    pairs-=1
                else:
                    i+=1
                if pairs==0:
                    return True
        ans = 10**20
        while l<=r:
            mid = (l+r)//2
            if is_possible(mid):
                ans = min(ans,mid)
                r = mid-1
            else:
                l = mid+1
        
        return ans
            


