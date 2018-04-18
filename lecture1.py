def find1Dpeak(arr):
  """
  Finds a 1D peak in a list of comparable types

  A 1D peak is an x in L such that it is greater
  than or equal to all its neighbors.

  ex. [1, 1, 2, 1] in this list, the elements at
  index 0 and index 2 are peaks.

  Complexity: O(log(n))
  where n = len(list)
  """
  n = len(arr)
  if n == 1:
    return arr[0]
  if n == 2:
    return arr[1] if arr[0] < arr[1] else arr[0]
  if arr[n / 2] < arr[(n / 2) - 1]:
    return find1Dpeak(arr[:n / 2])
  if arr[n / 2] < arr[(n / 2) + 1]:
    return find1Dpeak(arr[n / 2:])
  return arr[n / 2]

def find2Dpeak(plane):
  """
  Finds a 2D peak in a 2D list of comparable types

  A 2D peak is an x in P such that it is greater than
  or equal to both its horizontal and both its
  vertical neighbors

  ex.

  [1, 0, 0]
  [2, 2, 0]
  [0, 0, 0]

  the top right corner is a peak
  the middle left and middle right elements are peaks
  the bottom right corner is a peak

  Complexity: T(n, m) = T(n, m/2) + O(n) = O(n * log(m))
  where n = len(child_list) and m = len(parent_list)
  """
  n = len(plane)
  middle_row = plane[n / 2]
  middle_max = max(middle_row)
  i = middle_row.index(middle_max)
  if n == 1:
    return middle_max
  if n == 2:
    top_val = plane[0][i]
    return top_val if middle_max < top_val else middle_max
  if middle_max < plane[(n / 2) - 1][i]:
    return find2Dpeak(plane[n / 2:])
  if middle_max < plane[(n / 2) + 1][i]:
    return find2Dpeak(plane[:n / 2])
  return middle_max






