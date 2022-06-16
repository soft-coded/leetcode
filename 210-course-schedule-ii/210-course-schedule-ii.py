class Solution:
    def findOrder(self, courses: int, prereqs) -> List[int]:
      graph = [[] for i in range(courses)]
      # -1 = visiting, 1 = visited
      visited = [0 for i in range(courses)]
      ans = []
      
      for a, b in prereqs:
        graph[a].append(b)
        
      def dfs(node):
        if visited[node] == 1:
          return True
        if visited[node] == -1:
          return False
        
        visited[node] = -1
        
        while graph[node]: # while the node has dependecies
          dep = graph[node].pop()
          no_cycle = dfs(dep)
          if not no_cycle:
            return False
          
        visited[node] = 1
        ans.append(node)
        return True
      
      for i in range(courses):
        if not dfs(i):
          return []
      
      return ans
            
            
            