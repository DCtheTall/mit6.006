"""
Catalan number formula
Karatsuba multiplication
------------------------

This lecture series is the first in their module
on numerics algorithms

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

  Also can be written as C_n+1 = SUM C_i * C_n-i FROM i = 0 to n

  """
  return choose(2 * n, n) / (n + 1)


def karatsuba_multiply(a, b, precision=50, radix=10):
  """
  Karatsuba multiplication for integers

  Generalized for integers 0 <= a, b <= radix ** precision

  Complexity: O(n ^ log_2(3)) where n is the precision of multiplication desired

  """
  precision_on_2 = precision >> 1
  a_1 = a // (radix ** precision_on_2)
  a_0 = a - (a_1 * (radix ** precision_on_2))
  b_1 = b // (radix ** precision_on_2)
  b_0 = b - (a_1 * (radix ** precision_on_2))
  if a_0 == a or b_0 == b:
    return a * b
  c_2 = karatsuba_multiply(a_1, b_1, precision_on_2, radix)
  c_1 = karatsuba_multiply(a_1 + a_0, a_0 + b_1, precision_on_2, radix)
  c_0 = karatsuba_multiply(a_0, b_0, precision_on_2, radix)
  return (c_2 * (radix * precision)) \
    + ((c_1 - c_2 - c_0) * (radix ** precision_on_2)) \
    + c_0
