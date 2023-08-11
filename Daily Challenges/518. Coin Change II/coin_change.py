class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        @cache
        def combs(cur_amt,i):
            if cur_amt==amount:
                return 1
            if i==len(coins) or cur_amt>amount:
                return 0
            ans = combs(cur_amt,i+1)
            while cur_amt<=amount:
                ans+=combs(cur_amt+coins[i],i+1)
                cur_amt+=coins[i]
            return ans
        return combs(0,0)
            