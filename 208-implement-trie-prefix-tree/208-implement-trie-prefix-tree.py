class Node:
  def __init__(self):
    self.rels = [None] * 26
    self.is_end = False
  
  def insert(self, ch, node):
    self.rels[ord(ch) - ord('a')] = node
  
  def get(self, ch):
    return self.rels[ord(ch) - ord('a')]

class Trie:
    def __init__(self):
      self.root = Node()

    def insert(self, word: str) -> None:
      cur = self.root
      for item in word:
        if not cur.get(item):
          cur.insert(item, Node())
        cur = cur.get(item)
      cur.is_end = True
        
    def search(self, word: str) -> bool:
      cur = self.root
      for item in word:
        if not cur.get(item):
          return False
        cur = cur.get(item)
      return cur.is_end

    def startsWith(self, word: str) -> bool:
      cur = self.root
      for item in word:
        if not cur.get(item):
          return False
        cur = cur.get(item)
      return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)