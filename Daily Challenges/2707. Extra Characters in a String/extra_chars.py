class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        @cache
        def dp(start,i):
            if i == len(s)-1:
                cur_word = s[start:i+1]
                return len(cur_word) if cur_word not in words else 0
            else:
                cur_word = s[start:i+1]
                partition = dp(i+1,i+1)
                if cur_word not in words:
                    partition += len(cur_word)
                included = dp(start,i+1)
                return min(included,partition)
        return dp(0,0)