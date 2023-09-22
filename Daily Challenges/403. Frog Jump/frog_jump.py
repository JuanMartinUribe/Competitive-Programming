class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]-stones[0]>1:
            return False
        indexes = {unit:i for i,unit in enumerate(stones)}
        @cache
        def dp(i,last_jump):
            if i == len(stones)-1:
                return True
            elif i>=len(stones):
                return False
            else:
                short_jump = last_jump-1 
                long_jump = last_jump+1
                ans = False
                if stones[i]+short_jump in indexes and short_jump>0:
                    ans |= dp(indexes[stones[i]+short_jump],short_jump)
                if stones[i]+long_jump in indexes:
                    ans |= dp(indexes[stones[i]+long_jump],long_jump)
                if stones[i]+last_jump in indexes:
                    ans |= dp(indexes[stones[i]+last_jump],last_jump)
                return ans
        return dp(1,1)
