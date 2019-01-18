"""
Lecture 7: Linear Sorting
Counting Sort
-------------
This program contains an implementation of
counting sort, a linear time sorting algorithm.

"""


def counting_sort(k, arr):
  """
  Counting sort implementation for an array
  of integers in the range [0, k)

  """
  cache = [0 for _ in range(k)]
  for key in arr:
    cache[key] += 1
  result = []
  for key, count in enumerate(cache):
    for _ in range(count):
      result.append(key)
  return result


def counting_sort2(k, arr):
  """
  Another implementation of counting sort
  for lists of integers in the range [0, k)
  which uses nested lists

  Complexity: O(n + k)

  """
  cache = [[] for _ in range(k)]  # O(k)
  for e in arr:  # O(n)
    cache[e].append(e)
  output = []
  for key in range(k):  # O(k)
    output.extend(cache[key])
  return output
