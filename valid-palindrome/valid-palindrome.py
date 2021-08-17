class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for item in s:
          if item.isalnum():
            ns += item.lower()
        return ns == ns[::-1]