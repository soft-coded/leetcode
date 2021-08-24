class Solution:
    def detectCapitalUse(self, word: str) -> bool:
      u = word.upper()
      l = word.lower()
      c = word[0].upper() + word[1:].lower()
      return word == u or word == l or word == c