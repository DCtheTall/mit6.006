def swap(arr, i, j):
  """
  Swap elements in list arr at indices i and j

  Complexity: O(1)
  """
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
  return arr

def max_heapify(arr, i):
  """
  Max heapify a list arr at index i

  Complexity: O(log(n))
  One operation for each level of the tree deeper than the log(i)
  """
  left = i << 1
  right = left + 1
  largest = i
  if left < len(arr) and arr[largest] < arr[left]:
    largest = left
  if right < len(arr) and arr[largest] < arr[right]:
    largest = right
  if largest != i:
    swap(arr, i, largest)
    max_heapify(arr, largest)

def build_max_heap(arr):
  """
  Build a max heap out of list arr

  Complexity: O(n)
  Num operations = (c * n / 4) + ((2 * c) * (n / 8)) + ... + (log(n) * c)
  Let n / 4 = 2^k
  Num ops = 2^k * c * (1 / 2 + 1 / 4 + ... + (k + 1) / 2^k)
  The third term in the product is bounded by a constant
  So num ops converges to 2^k * C where C is some constant
  So therefore num ops is propto n
  """
  i = len(arr) / 2
  while i > -1:
    max_heapify(arr, i)
    i -= 1
  return arr
