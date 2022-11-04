#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        ans = 0
        n = len(grid)
        m = len(grid[0])
        
        def bfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1:
                return
            
            grid[i][j] = -1
            
            for row in range(-1, 2):
                for col in range(-1, 2):
                    bfs(i + row, j + col)
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    bfs(i, j)
                    ans += 1
                
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends