
class Solution:
    def trappingWater(self, h,n):
      n = len(h)
      mxs = [0] * n
      left = right = 0
      
      for i in range(n):
        mxs[i] = left
        left = max(left, h[i])
      
      for i in range(n - 1, -1, -1):
        mnh = min(right, mxs[i])
        if h[i] < mnh:
          mxs[i] = mnh - h[i]
        else:
          mxs[i] = 0
        right = max(right, h[i])
      
      return sum(mxs)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends