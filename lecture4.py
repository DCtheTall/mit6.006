"""
Heaps
-----

"""


def max_heapify(arr, i, N):
  """
  Max heapify a list arr from index N-1 to index i

  Complexity: O(log(N))
  One operation for each level of the tree deeper than the log(i)

  """
  left = i << 1
  right = left + 1
  largest = i
  if left < N and arr[largest] < arr[left]:
    largest = left
  if right < N and arr[largest] < arr[right]:
    largest = right
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    max_heapify(arr, largest, N)


def build_max_heap(arr):
  """
  Build a max heap out of list arr

  Complexity: O(n) where n = len(arr)
  Num operations = (c * n / 4) + ((2 * c) * (n / 8)) + ... + (log(n) * c)
  Let n / 4 = 2^k
  Num ops = 2^k * c * (1 / 2 + 1 / 4 + ... + (k + 1) / 2^k)
  The third term in the product is bounded by a constant
  So num ops converges to 2^k * C where C is some constant
  So therefore num ops is propto n

  """
  for i in range(len(arr) / 2, -1, -1):
    max_heapify(arr, i, len(arr))
  return arr


def heap_sort(arr):
  """
  Heap sort a list arr

  Complexity: O(n * log(n)) where n = len(arr)
  build_max_heep is O(n)
  Then iterate over each element of arr:
    - Call swap: O(1)
    - max_heapify: O(log(N)) for N in 1 to n

  """
  build_max_heap(arr)
  for i in range(len(arr) - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    max_heapify(arr, 0, i)
  return arr
