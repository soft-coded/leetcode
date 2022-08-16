class Solution:
  def maximumUnits(self, boxes: List[List[int]], total: int) -> int:
    boxes.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for box in boxes:
      curmax = min(total, box[0])
      ans += curmax * box[1]
      total -= curmax
    return ans