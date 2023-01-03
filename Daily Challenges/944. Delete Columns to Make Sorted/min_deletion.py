class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        last_row = collections.defaultdict(str)
        dels = 0
        N = len(strs[0])
        for col in range(N):
            last_letter = 'a'
            for j,s in enumerate(strs):
                if s[col]<last_letter:
                    dels+=1
                    break
                last_letter=s[col]     
        return dels