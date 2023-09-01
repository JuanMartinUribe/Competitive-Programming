class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for bit in range(n+1):
            ones = str(bin(bit)).count("1")
            ans.append(ones)
        return ans