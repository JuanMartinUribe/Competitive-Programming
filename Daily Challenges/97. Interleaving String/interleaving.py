class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def intervals(i,j,k):
            if i==len(s1) and j==len(s2) and k==len(s3):
                return True
            elif k == len(s3):
                return False
            else:
                ans = False
                if i<len(s1) and s1[i]==s3[k]:
                    ans |= intervals(i+1,j,k+1)
                if j<len(s2) and s2[j]==s3[k]:
                    ans |= intervals(i,j+1,k+1)
                return ans
        return intervals(0,0,0)