def swap(arr, i, j):
  """
  Swap elements in list arr at indices i and j

  Complexity: O(1)
  """
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
  return arr

def max_heapify(arr, N, i):
  """
  Max heapify a list arr from index N to index i

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
    swap(arr, i, largest)
    max_heapify(arr, N, largest)

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
  i = len(arr) / 2
  while i > -1:
    max_heapify(arr, len(arr), i)
    i -= 1
  return arr

def heap_sort(arr):
  """
  Heap sort a list arr

  Complexity: O(n * log(n)) where n = len(arr)
  build_max_heep is O(n)
  Then iterate over each element of arr:
    - Call swap: O(1)
    - max_heapify: O(log(N))
  """
  build_max_heap(arr)
  N = len(arr)
  while N > 0:
    N -= 1
    swap(arr, 0, N)
    max_heapify(arr, N, 0)
  return arr
