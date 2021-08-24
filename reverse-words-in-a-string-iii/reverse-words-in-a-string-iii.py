class Solution:
    def reverseWords(self, s: str) -> str:
        sent = s.split()
        for i in range(len(sent)):
          re = list(sent[i])
          re.reverse()
          sent[i] = ''.join(re)
        return " ".join(sent)