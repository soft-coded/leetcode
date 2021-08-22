class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [0] * n
        f = "Fizz"; b = "Buzz"; fb = "FizzBuzz"
        for i in range(n):
          if (i + 1) % 15 == 0: ans[i] = fb
          elif (i + 1) % 5 == 0: ans[i] = b
          elif (i + 1) % 3 == 0: ans[i] = f
          else: ans[i] = str(i + 1)
        return ans