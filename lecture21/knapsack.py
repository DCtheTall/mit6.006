"""
Dynamic Programing III:
The Knapsack Problem
--------------------
This program contains an algorithm which solves the
knapsack problem. The prodlem is defined as:

You have a knapsack with a maximum capacity (capacity)
that you can put in items, each with an associated
weight (int) and value (number). What is the maximum
value you can put in the knapsack given the constraint:

sum(weights of items in knapsack) <= capacity

"""

def get_optimal_knapsack_value(W, items):
  """
  Gets the highest value the knapsack can carry
  given items of the form [(weight, value)]
  up to a weight W

  Complexity: O(n * S)

  """
  n = len(items)
  knapsacks = dict()
  for i in range(n, -1, -1):
    for j in range(W + 1):
      if i == n:
        knapsacks[(i, j)] = 0
        continue
      if j == 0:
        knapsacks[(i, j)] = 0
        continue
      weight, value = items[i]
      if weight <= j:
        knapsacks[(i, j)] = max(
          knapsacks[(i + 1, j)],
          knapsacks[(i + 1, j - weight)] + value)
      else:
        knapsacks[(i, j)] = knapsacks[(i + 1, j)]
  return knapsacks[(0, W)]
