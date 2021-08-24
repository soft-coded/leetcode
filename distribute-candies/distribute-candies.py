class Solution:
    def distributeCandies(self, ct: List[int]) -> int:
        s = set(ct)
        return len(s) if len(ct) // 2 > len(s) else len(ct) // 2