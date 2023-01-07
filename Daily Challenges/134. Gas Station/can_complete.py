class Solution:
    def canCompleteCircuit(self, gas_list: List[int], cost_list: List[int]) -> int:
        dp = [-1]*len(gas_list)
        left = len(dp)
        for i in range(2):
            if -1 not in dp: return (left+1)%len(dp)
            for index,(cost,gas) in enumerate(zip(cost_list,gas_list)):
                prev = index-1 if index>0 else len(gas_list)-1
                flag = True if dp[index]==-1 else False
                if dp[prev]==-1:
                    dp[index] = max(gas-cost,-1)
                else:
                    dp[index] = max(gas-cost,dp[prev]+gas-cost,-1)
                if flag and dp[index]>-1:
                    left=index         
        print(dp)
        return left+1 if -1 not in dp else -1