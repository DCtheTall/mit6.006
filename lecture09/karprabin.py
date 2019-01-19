"""
Lecture 9: Karp-Rabin
---------------------
This lecture contains an implementation
of the Karp-Rabin search algorithm to
test string equality.

"""


def is_prime(n):
  """
  Miller-Rabin primality test
  for n < 2 ** 64

  """
  test_vals = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
  if n in test_vals:
    return True
  d = n - 1
  s = 0
  while not d & 1:
    d = d >> 1
    s += 1
  for a in test_vals:
    for r in range(0, s):
      if (a ** (d * (1 << r))) % n != (n - 1) \
              and (a ** d) % n != 1:
          return False
  return True


def get_larger_prime(n):
  """
  Get a prime number larger than n
  Not guaranteed to be the next prime

  """
  result = n + (1 if n % 2 == 0 else 2)
  while not is_prime(result):
    result += 2
  return result


def simple_text_search(s, t):
  """
  Linear search through the string
  for substr s in str t

  Complexity: O(len(s) * len(t)) <- not so good

  """
  return any([s == t[i:i + len(s)] for i in range(len(t) - len(s))])


class RollingHash:
  """
  An object which keeps track of a polynomial
  hash for a string with characters in the
  ASCII character set

  """
  def __init__(self, min_size):
    self.hash = 0
    self.size = 0
    self.base = get_larger_prime(min_size)

  def append(self, c):
    self.hash *= 256
    self.hash += ord(c) % self.base
    self.size += 1

  def pop_left(self):
    self.size -= 1
    self.hash %= 256 ** self.size


def karp_rabin_search(s, t):
  """
  Karp-Rabin search implmented for strings with
  characters in the ASCII set

  Complexity: O(len(s) + len(t))

  """
  rs = RollingHash(len(s))
  rt = RollingHash(len(s))
  for c in s:
    rs.append(c)
  for c in t[:len(s)]:
    rt.append(c)
  if rs.hash == rt.hash:
    return True
  for i in range(len(s), len(t)):
    rt.pop_left()
    rt.append(t[i])
    if rs.hash == rt.hash:
      return True
  return False
