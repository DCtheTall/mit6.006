def insertion_sort(arr):
  """
  Insertion sort implementation

  Complexity: O(n ** 2)
  """
  for i in range(1, len(arr)):
    for j in range(0, i):
      if arr[i - j] < arr[i - j - 1]:
        tmp = arr[i - j]
        arr[i - j] = arr[i - j - 1]
        arr[i - j - 1] = tmp
  return arr

# Merge sort
# From: https://en.wikipedia.org/wiki/Merge_sort

def merge(left, right):
  """
  Merge two sorted arrays into a single sorted array

  Complexity: O(n + m)
  where n = len(left) and m = len(right)
  """
  result = []
  while left and right:
    if left[0] < right[0]:
      result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]
  while left:
    result.append(left[0])
    left = left[1:]
  while right:
    result.append(right[0])
    right = right[1:]
  return result

def merge_sort(arr):
  n = len(arr)
  if n <= 1:
    return arr
  left = []
  right = []
  for i, x in enumerate(arr):
    if i < n / 2:
      left.append(x)
    else:
      right.append(x)
  left = merge_sort(left)
  right = merge_sort(right)
  return merge(left, right)
