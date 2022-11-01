class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        heap = []
        
        for key, val in c.items():
            heappush(heap, (-val, key))
        
        ans = ""
        while heap:
            freq, char = heappop(heap)
            freq *= -1
            ans += char * freq
        
        return ans