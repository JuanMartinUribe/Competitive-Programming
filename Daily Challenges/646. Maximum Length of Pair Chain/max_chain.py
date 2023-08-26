class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p:p[1])
        chain = 1
        r = pairs[0][1]
        for nl,nr in pairs:
            if r<nl:
                chain+=1
                r = nr
        return chain