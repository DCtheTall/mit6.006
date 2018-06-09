"""
Dynamic Programing III:
=======================

1. Matrix Multiplication Optimization
-------------------------------------

Matrix multiplication is associative, i.e.

A * (B * C) = (A * B) * C

Changing the order in which matrices are evaluated
can change the number of operations a computer
can do to calculate them.

For this algorithm, the size of the matrix is all
we are concerned with, so we can represent them
with tuples of 2 ints.

Let (n, m) be an n * m matrix.

"""


def multiply(A, B):
  """
  Calculate the number of operations to
  multiply two matrices and the size of
  the resulting matrix:

  returns (c, (n * m))
  where c is the number of scalar multiplications performed
  and n, m represent the size of the resulting matrix

  """
  rowsA, colsA = A
  rowsB, colsB = B
  if colsA != rowsB:
    return (float('inf'), (None, None))
  return (rowsA * colsA * colsB, (rowsA, colsB))


def multiply_matrices(*matrices):
  """
  Extends the function above for multiplying
  more than 2 matrices

  """
  A = matrices[0]
  total_cost = 0
  for B in matrices[1:]:
    (cost, A) = multiply(A, B)
    total_cost += cost
  return (total_cost, A)


def multiply_nested_matrices(*matrices):
  """
  Extends the function above to multiply
  matrices where some arguments may be
  matrices nested in tuples, representing
  a multiplication with parentheses

  """
  A = matrices[0]
  total_cost = 0
  if isinstance(A[0], tuple):
    (cost, A) = multiply_nested_matrices(*A)
    total_cost += cost
  for B in matrices[1:]:
    if isinstance(B[0], tuple):
      (cost, B) = multiply_nested_matrices(*B)
      total_cost += cost
    (cost, A) = multiply(A, B)
    total_cost += cost
  return (total_cost, A)


def naive_optimal_matrix_multiplication(*matrices):
  """
  Get the optimal matrix multiplication order
  for a list of matrices using the naive
  recursive method which tries every possible
  parenthesization

  returns (c, optimal_order)
  where c is the min number of scalar multiplications
  needed to multiply the matrices
  and optimal_order is a tuple of nested matrix tuples
  representing the optimal parenthesization

  Complexity: O(2 * (2 ** n)) = O(4 ** n) (exponential time, bad)

  """
  n = len(matrices)
  (cost, _) = multiply_nested_matrices(*matrices)
  orders = {cost: matrices}
  for k in range(1, n - 1):
    left = matrices[:k]
    right = matrices[k:]
    (_, left_order) = naive_optimal_matrix_multiplication(*left)
    if len(left_order) < 2:
      left_order = left_order[0]
    (_, right_order) = naive_optimal_matrix_multiplication(*right)
    if len(right_order) < 2:
      right_order = right_order[0]
    (cost, _) = multiply_nested_matrices(left_order, right_order)
    if cost not in orders:
      orders[cost] = (left_order, right_order)
  return (min(orders), orders[min(orders)])


def dp_optimal_matrix_multiplication(*matrices):
  """
  Solving the same problem as the above
  function using dynamic programming

  It iterates over every substring of the
  matrices tuple and calculates the optimal
  way to multiply those

  returns (c, optimal_order)
  where c is the min number of scalar multiplications
  needed to multiply the matrices
  and optimal_order is a tuple of nested matrix tuples
  representing the optimal parenthesization

  Complexity: O(n ** 3) (polynomial time, better)

  """
  n = len(matrices)
  optimal_costs = {}
  products = {}
  optimal_orders = {}
  for step in range(n):
    for i in range(n - step):
      j = i + step
      if step == 0:
        optimal_costs[(i, j)] = 0
        products[(i, j)] = matrices[i]
        optimal_orders[(i, j)] = matrices[i]
        continue
      if step == 1:
        (cost, result) = multiply(matrices[i], matrices[j])
        optimal_costs[(i, j)] = cost
        products[(i, j)] = result
        optimal_orders[(i, j)] = (matrices[i], matrices[j])
        continue
      costs = {}
      for k in range(i + 1, j + 1):
        cost = optimal_costs[(i, k - 1)]
        cost += optimal_costs[(k, j)]
        (_, result1) = multiply_matrices(*matrices[i:k])
        (_, result2) = multiply_matrices(*matrices[k:j + 1])
        (c, result) = multiply(result1, result2)
        cost += c
        if (i, j) not in products:
          products[(i, j)] = result
        costs[cost] = k
      best_cost = min(costs)
      optimal_costs[(i, j)] = best_cost
      k = costs[best_cost]
      optimal_orders[(i, j)] = (optimal_orders[(i, k - 1)], optimal_orders[(k, j)])
  return (optimal_costs[(0, n - 1)], optimal_orders[(0, n - 1)])
