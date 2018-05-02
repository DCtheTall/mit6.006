"""
Linear (or integer) sorting in linear time (best case)

"""


def counting_sort(k, arr):
  """
  Counting sort implementation for an array
  of integers in the range [0, k)
  """
  cache = [0] * k
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
  cache = [[] for _ in range(k)] # O(k)
  for e in arr: # O(n)
    cache[e].append(e)
  output = []
  for key in range(k): # O(k)
    output.extend(cache[key])
  return output


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

