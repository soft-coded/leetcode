from math import inf
from heapq import *

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dist = [inf] * V
        dist[S] = 0
        heap = []
        heappush(heap, (0, S)) # (distance, node)
        # adj = [[[1, 9]], [[0, 9]]]
        while heap:
            distance, node = heappop(heap)
            
            for nei_node, nei_weight in adj[node]:
                if dist[node] + nei_weight < dist[nei_node]:
                    dist[nei_node] = dist[node] + nei_weight
                    heappush(heap, (dist[nei_node], nei_node))
        
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