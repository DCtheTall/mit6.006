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


def multiply_matrices(A, B):
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


def optimal_matrix_multiplication(matrices):
  """
  Get the optimal matrix multiplication order
  for a list of matrices

  returns (c, multiplication_order)
  where c is the minimum number of scalar
  multiplications needed
  and multiplication_order is a list
  of tuples of 2 ints

  """
  pass


