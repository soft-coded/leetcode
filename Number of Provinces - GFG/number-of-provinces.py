#User function Template for python3

def get_list(mat):
    adj = {}
    
    for i in range(len(mat)):
        adj[i + 1] = []
        for j in range(len(mat[0])):
            if mat[i][j]:
                adj[i + 1].append(j + 1)
    
    return adj

class Solution:
    def numProvinces(self, mat, V):
        ans = 0
        visited = set()
        adj = get_list(mat)
        
        def dfs(node):
            visited.add(node)
            
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        for node in range(1, V + 1):
            if node not in visited:
                ans += 1
                dfs(node)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends