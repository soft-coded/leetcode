class Solution:
  def findJudge(self, N, trust):
    graph = [0] * (N + 1)
    for i, j in trust:
      graph[i] -= 1
      graph[j] += 1
    for i in range(1, N + 1):
      if graph[i] == N - 1:
        return i
    return -1