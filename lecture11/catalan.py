"""
Lecture 11: Karatsuba Multiplication
Catalan Number Formula
----------------------
This program contains a function for
calculating the n^th Catalan number.

"""


def factorial(n):
  """
  Compute n factorial (n!)

  """
  return 1 if n <= 1 else n * factorial(n - 1)


def choose(n, m):
  """
  n Choose m

  """
  return factorial(n) / factorial(n - m) / factorial(m)


def catalan(n):
  """
  Calculate the n^th (starting w 0) Catalan number
  Also can be written as C_n+1 = SUM C_i * C_n-i FROM i = 0 TO n

  """
  return choose(2 * n, n) / (n + 1)
