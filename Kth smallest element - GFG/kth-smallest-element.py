#User function Template for python
from heapq import *

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

class Solution:
    def kthSmallest(self,arr, l, r, k):
        heapify(arr)
        while k > 1:
            heappop(arr)
            k -= 1
        return heappop(arr)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends