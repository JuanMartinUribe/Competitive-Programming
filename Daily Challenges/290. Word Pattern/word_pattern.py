class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters_lookup = collections.defaultdict(str)
        words_lookup = collections.defaultdict(str)
        letters,words = list(pattern),s.split(' ')

        if len(letters)!=len(words):return False
        
        for letter,word in zip(letters,words):
            if letter not in letters_lookup and word not in words_lookup:
                letters_lookup[letter]=word
                words_lookup[word]=letter
            elif letters_lookup[letter]!=word or words_lookup[word]!=letter:
                return False
        return True

        










