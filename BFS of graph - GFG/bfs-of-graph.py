#User function Template for python3
from collections import deque


class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        visited = set()
        ans = []
        dq = deque()
        dq.append(0)
        
        while dq:
            vertex = dq.popleft()
            if vertex in visited:
                continue
            
            ans.append(vertex)
            visited.add(vertex)
            
            for neighbour in adj[vertex]:
                dq.append(neighbour)
        
        return ans

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends