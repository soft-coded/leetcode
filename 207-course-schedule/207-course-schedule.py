class Solution:
    def canFinish(self, courses: int, prereqs) -> bool:
      graph = [[] for i in range(courses)]
      visited = [0 for i in range(courses)]
      
      for a, b in prereqs:
        graph[a].append(b)
        
      def dfs(node):
        if visited[node] == 1: # already visited
          return True
        if visited[node] == -1: # currently visiting the node
          return False # this indicates a cycle
        visited[node] = -1
        for dep in graph[node]:
          no_cycle = dfs(dep)
          if not no_cycle:
            return False
        visited[node] = 1
        return True
      
      for i in range(courses):
        if not dfs(i):
          return False
      return True
      