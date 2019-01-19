"""
Lecture 19: Dynamic programming I:
Fibonacci
---------
This program contains 3 different implementations
of computing the n^th Fibonacci number:

1. An exponential time naive recursive algorithm.
2. A memoized dynamic programming algorithm.
3. A bottom-up dynamic programming algorithm.

"""


def naive_fibonacci(n):
  """
  Naive recursion algorithm for n >= 0

  Complexity: exponential time (bad)

  """
  if n == 0 or n == 1:
    return n
  return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)


memoization_table = dict()

def memoized_fibonnaci(n):
  """
  Memoized fibonacci reduces computation
  time by saving each computed value

  Complexity: linear time (good)
  Justification:

  Calling fib(n) the naive way creates the
  recursion tree (in Lisp notation):

  (fib(n)
    (fib(n - 1)
      (fib(n - 2) (...) (...))
      (...))
    (fib(n - 2)
      (fib(n - 3)
        (fib(n - 4) (...) (...))
        (...))
      (...)))

  Memoization removes the need for the right
  child of every subtree, which turns the
  recursion tree into a linked list of length n

  """
  if n in memoization_table:
    return memoization_table[n]
  if n == 0 or n == 1:
    return n
  else:
    f = memoized_fibonnaci(n - 1) + memoized_fibonnaci(n - 2)
  memoization_table[n] = f
  return f


def bottom_up_fibonacci(n):
  """
  Bottom up fibonacci using
  for loop instead of recursion

  This method avoids recursion
  and is more space efficient
  than using a dictionary

  The drawback to this algorithm
  versus the one above is that
  this algorithm does not memoize
  results from previous calls

  Complexity: constant space, linear time

  """
  if n < 2:
    return n
  fib = [0, 1]
  for _ in range(2, n):
    fib = [fib[1], sum(fib)]
  return sum(fib)
