class Solution:
  def asteroidsDestroyed(self, mass: int, asteroids: List[int]):
    asteroids.sort()
    i = 0
    while i < len(asteroids) and asteroids[i] <= mass:
      mass += asteroids[i]
      i += 1
    
    return i == len(asteroids)