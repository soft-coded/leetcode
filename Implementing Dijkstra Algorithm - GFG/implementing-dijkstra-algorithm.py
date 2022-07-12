from math import inf
from heapq import *

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    # O((V + E) * log V) time
    def dijkstra(self, V, adj, S):
        # adj = [[[1, 9]], [[0, 9]]]
        dist = [inf] * V
        dist[S] = 0
        # (dist, node)
        heap = [(0, S)]
        
        while heap:
            _, node = heappop(heap)
            
            for nei, nei_w in adj[node]:
                sm = dist[node] + nei_w
                if dist[node] + nei_w < dist[nei]:
                    dist[nei] = sm
                    heappush(heap, (dist[nei], nei))
        
        return dist
                    
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends