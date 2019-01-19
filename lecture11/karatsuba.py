"""
Lecture 11: Karatsuba Multiplication
------------------------------------
This program contains an implementation of
Karatsuba multiplication, an efficient
divide-and-conquer algorithm for high
precision multiplication.

"""


def karatsuba_multiply(a, b, precision=50, radix=10):
  """
  Karatsuba multiplication for integers
  Generalized for integers 0 <= a, b <= radix ** precision
  Complexity: O(n ^ log_2(3)) where n is the precision of
  multiplication desired.

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
