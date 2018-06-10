"""
Dynamic Programing III:
=======================

1. Edit Distance
----------------

Find the optimal way to change a string: str1
to be equal to a second string: str2
with the lowest cost.

Since cost of operations can be defined arbitrarily,
I will outline how I do it here, of course, if you
define cost differently the algorithm holds

Cost of insert: 1
Cost of delete: 1
Cost of replace: 2 (replace is a delete then insert)

"""


def dp_edit_distance(str1, str2):
  """
  Finds the minimum edit displace between
  two strings

  I use 1

  """
  n = len(str1)
  m = len(str2)
  optimal_costs = {}
  i = n - 1
  j = m - 1
  for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
      if str1[i] == str2[j]:
        if i == n - 1 and j == m - 1:
          optimal_costs[(i, j)] = 0
        elif i == n - 1:
          optimal_costs[(i, j)] = optimal_costs[(i, j + 1)]
        elif j == m - 1:
          optimal_costs[(i, j)] = optimal_costs[(i + 1, j)]
        else:
          optimal_costs[(i, j)] = optimal_costs[(i + 1, j + 1)]
      elif i == n - 1 and j == m - 1:
        optimal_costs[(i, j)] = 2 if n == m else 1
      elif i == n - 1:
        optimal_costs[(i, j)] = 1 + optimal_costs[(i, j + 1)]
      elif j == m - 1:
        optimal_costs[(i, j)] = 1 + optimal_costs[(i + 1, j)]
      else:
        optimal_costs[(i, j)] = min(
          1 + optimal_costs[(i + 1, j)], # cost of delete
          1 + optimal_costs[(i, j + 1)], # cost of insert
          2 + optimal_costs[(i + 1, j + 1)], # cost of replace
        )
  return optimal_costs[(0, 0)]
