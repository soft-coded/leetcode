#User function Template for python3
from bisect import bisect_left, bisect_right

def find(arr,n,x):
    ans = [-1, -1]
    left = bisect_left(arr, x)
    right = bisect_right(arr, x) - 1
    if left >= len(arr):
        return ans
    if arr[left] == x:
        ans[0] = left
    if arr[right] == x:
        ans[1] = right
    return ans

#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends