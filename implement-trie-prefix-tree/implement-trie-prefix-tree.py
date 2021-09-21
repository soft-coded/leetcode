class Node:
  def __init__(self):
    self.links = [None] * 26
    self.is_end = False
  
  def get(self, key):
    return self.links[ord(key) - ord('a')]
  
  def put(self, key, node):
    self.links[ord(key) - ord('a')] = node
    
  def set_end(self):
    self.is_end = True

class Trie:
    def __init__(self):
      self.root = Node()
        
    def insert(self, word: str) -> None:
      cur = self.root
      for item in word:
        if not cur.get(item):
          cur.put(item, Node())
        cur = cur.get(item)
      cur.set_end()
      
    def prefix(self, word):
      cur = self.root
      for item in word:
        if cur.get(item):
          cur = cur.get(item)
        else: return None
      return cur

    def search(self, word: str) -> bool:
      cur = self.prefix(word)
      return cur and cur.is_end

    def startsWith(self, word: str) -> bool:
      cur = self.prefix(word)
      return cur is not None