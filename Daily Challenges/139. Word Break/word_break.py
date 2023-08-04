class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        @cache
        def splits(i,start_index): 
            if i==len(s) and start_index==i:
                return True
            if i == len(s):
                return False
            included = False
            cur_s = s[start_index:i+1]
            if cur_s in words:
                included = splits(i+1,i+1)
            return included or splits(i+1,start_index)
        return splits(0,0)