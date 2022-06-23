#User function Template for python3
import math

def getMinMax(a, n):
    mx = -math.inf
    mn = math.inf
    for item in a:
        mx = max(mx, item)
        mn = min(mn, item)
    return mn, mx

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends