"""
QuickSort
---------

"""


def partition(L, lo, hi):
  """
  Partition a list from lo index to hi index
  runs in linear time

  """
  pivot = L[hi]
  i = lo - 1
  for k in range(lo, hi):
    if L[k] < pivot:
      i += 1
      L[i], L[k] = L[k], L[i]
  L[i + 1], L[hi] = L[hi], L[i + 1]
  return i + 1


def quicksort(L, lo, hi):
  """
  Quicksort a list from lo index to hi index
  to sort full list do quicksort(L, 0, len(L) - 1)

  Complexity:
  - Each partition runs in linear time
  - Then the array is split into two parts and each part is partitioned

  First pass: n operations
  Second pass: 2 * (n / 2) = n ops
  ...
  ~log(n)^th pass: n ops

  So the time complexity is O(n * log(n))
  """
  if lo < hi:
    p = partition(L, lo, hi)
    quicksort(L, lo, p - 1)
    quicksort(L, p + 1, hi)

