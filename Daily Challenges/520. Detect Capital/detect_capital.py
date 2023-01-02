class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = 0
        for w in word:
            if w.isupper():
                cnt+=1
        if cnt==0 or cnt==len(word) or (cnt==1 and word[0].isupper()):
            return True
        return False