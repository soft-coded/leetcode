from collections import deque

def bfs_check(n, adj, colors):
    dq = deque()
	dq.append(n)
	colors[n] = 0
	
	while dq:
	    node = dq.popleft()
	    
	    for nei in adj[node]:
	        if colors[nei] == -1:
	            colors[nei] = 1 - colors[node]
	            dq.append(nei)
            elif colors[nei] == colors[node]:
                return False
    
    return True

class Solution:
	def isBipartite(self, V, adj):
		colors = [-1] * V
		
		for i in range(V):
		    if colors[i] == -1 and not bfs_check(i, adj, colors):
                return False
        
        return True

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends