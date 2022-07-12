class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
      colours = [-1] * len(graph)
      
      def bfs(node):
        dq = deque()
        dq.append(node)
        colours[node] = 1
        
        while dq:
          cur = dq.popleft()
          
          for neighbour in graph[cur]:
            if colours[neighbour] == -1:
              colours[neighbour] = 1 - colours[cur]
              dq.append(neighbour)
            
            elif colours[neighbour] == colours[cur]:
              return False
        
        return True
      
      for i in range(len(graph)):
        if colours[i] == -1 and not bfs(i):
          return False
      
      return True