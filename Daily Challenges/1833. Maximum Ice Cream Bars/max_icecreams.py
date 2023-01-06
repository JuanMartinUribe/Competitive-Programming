class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        icecreams = 0
        while costs and coins>=costs[-1]:
            coins -= costs.pop()
            icecreams+=1
        return icecreams