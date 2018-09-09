"""
String matching
---------------

"""


from lecture08 import get_larger_prime, is_prime


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
