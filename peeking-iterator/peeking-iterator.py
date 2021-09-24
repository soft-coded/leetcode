# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, it):
        self.nums = []
        while it.hasNext():
          self.nums.append(it.next())
        self.ind = 0

    def peek(self):
        return self.nums[self.ind]
        

    def next(self):
        self.ind += 1
        return self.nums[self.ind - 1]
        

    def hasNext(self):
        return self.ind != len(self.nums)