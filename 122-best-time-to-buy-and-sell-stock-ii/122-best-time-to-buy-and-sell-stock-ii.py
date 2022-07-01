class Solution:
    def maxProfit(self, A: List[int]) -> int:
        n = len(A)
        last_buy = -A[0]
        last_sold = 0
                                
        for i in range(1, n):
            cur_buy = max(last_buy, last_sold - A[i])
            cur_sold = max(last_sold, last_buy + A[i])
            last_buy = cur_buy
            last_sold = cur_sold
        
        return last_sold