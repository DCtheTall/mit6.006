"""
Lecture 7: Linear Sorting
Counting Sort
-------------
This program contains an implementation of
radix sort, a linear time sorting algorithm.

"""

def binary_radix_sort(k, arr):
  """
  Radix sort for base 2 for a
  list of integers in the range [0, k)

  """
  i = 0
  while (1 << i) < k:
    buckets = [[], []]
    for key in arr:
      digit = (key // (1 << i)) & 1
      buckets[digit].append(key)
    arr = []
    for j in range(2):
      for key in buckets[j]:
        arr.append(key)
    i += 1
  return arr


def radix_sort(k, arr, base=2):
  """
  Radix sort for an arbitrary base
  Sorts a list of integers in [0, k)

  """
  i = 0
  while (base ** i) < k:
    buckets = [[] for j in range(base)]
    for key in arr:
      digit = (key // (base ** i)) % base
      buckets[digit].append(key)
    arr = []
    for j in range(base):
      for key in buckets[j]:
        arr.append(key)
    i += 1
  return arr
