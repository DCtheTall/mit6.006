"""
Lecture 3: Sorting
Insertion Sort
--------------
This program contains two implemenations
of the insertion sort algorithm.

"""


def insertion_sort(L):
  """
  Insertion sort implementation

  Complexity: O(n ** 2)

  """
  for i in range(1, len(L)):
    for j in range(0, i):
      if L[i - j] < L[i - j - 1]:
        L[i - j],  L[i - j - 1] = L[i - j - 1], L[i - j]
  return L


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
