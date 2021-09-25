class Solution:
    def mostCommonWord(self, p: str, bnd: List[str]) -> str:
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in p])
        words = normalized_str.split()
        word_count = defaultdict(int)
        banned_words = set(bnd)
        for word in words:
            if word not in banned_words:
                word_count[word] += 1
        return max(word_count.items(), key=operator.itemgetter(1))[0]