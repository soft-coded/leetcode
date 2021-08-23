class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = sorted(score, reverse = True)
        d = {}
        for i in range(len(arr)):
          d[arr[i]] = i + 1
        ans = []
        for item in score:
          if item == arr[0]:
            ans.append("Gold Medal")
          elif item == arr[1]:
            ans.append("Silver Medal")
          elif item == arr[2]:
            ans.append("Bronze Medal")
          else: ans.append(str(d[item]))
        return ans