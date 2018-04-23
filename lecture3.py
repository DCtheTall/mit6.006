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


def insertion_sort2(L):
  """
  Slightly improved insertion sort

  Complexity: O(n ** 2)
  """
  for i in range(len(L)):
    key = L[i]
    j = i - 1
    while j > -1 and L[j] > key:
      L[j + 1] = L[j]
      j -= 1
    L[j + 1] = key
  return L

# Merge sort
# From: https://en.wikipedia.org/wiki/Merge_sort

def merge(left, right):
  """
  Merge two sorted arrays into a single sorted array

  Complexity: O(n + m)
  where n = len(left) and m = len(right)
  """
  i = 0
  j = 0
  result = []
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  if i < len(left):
    result.extend(left[i:])
  if j < len(right):
    result.extend(right[j:])
  return result

def merge_sort(L):
  """
  Merge sort

  Complexity: O(n * log(n))
  where n = len(arr)
  """
  n = len(L)
  if n < 2:
    return L
  left = merge_sort(L[:n / 2])
  right = merge_sort(L[n / 2:])
  return merge(left, right)

"""
Functional merge sort

My own implementation of a pure functional merge sort
that can be expressed solely with lambda expressions
(it can be shown the list operations I used can be
expressed as functions). I use `if` control flow
to avoid writing ugly ternaries.

The above implementation is faster
and runs less risk of stack overflow.
This is more of an academic exercise.
"""

def func_merge(left, right):
  if not left:
    return right
  if not right:
    return left
  if left[0] < right[0]:
    return left[:1] + func_merge(left[1:], right)
  return right[:1] + func_merge(left, right[1:])

def func_merge_sort(L):
  if len(L) < 2:
    return L
  return func_merge(
    func_merge_sort(L[:len(L) / 2]),
    func_merge_sort(L[len(L) / 2:]),
  )
