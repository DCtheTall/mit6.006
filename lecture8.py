"""
Lecture 8: Hashing
------------------

"""

from random import randint

def is_prime(n):
  """
  Miller-Rabin primality test
  for n < 2 ** 64
  """
  test_vals = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
  d = n - 1
  s = 0
  while not d % 2:
    d /= 2
    s += 1
  for a in test_vals:
    for r in range(0, s):
      if ((a ** (d * (1 << r))) % n) != (n - 1) and (a ** d) % n != 1:
        return False
  return True

class Node:
  """
  Linked list node
  """
  def __init__(self, value):
    self.value = value
    self.next = None # should be set to a

class HashTable:
  """
  Hash table with chaining
  that stores objects in a table with length size (int)
  """
  def __init__(self, size):
    """
    Create a hash table of a provided size (int)
    """
    self.cache = [None for _ in range(size)]
    self.size = size
    self.lg_size = 0
    while size > 1:
      size = size >> 1
      self.lg_size += 1
    # For multiplication method
    self.mult_constant = randint(
      (1 << (self.lg_size - 1)) + 1,
      (1 << self.lg_size) - 1
    )
    # For universal hash method
    self.large_prime = (self.size + 2) if self.size % 2 else (self.size + 3)
    while not is_prime(self.large_prime):
      self.large_prime += 2
    self.univ_a = randint(0, self.large_prime - 1)
    self.univ_b = randint(0, self.large_prime - 1)

  def _search(self, hash_value, value):
    """
    Search a table for a given value given
    its hash, assumes objects have
    defined equality
    """
    if self.cache[hash_value] is None:
      return False
    curr = self.cache[hash_value]
    while curr is not None:
      if curr.value == value:
        return True
      curr = curr.next
    return False

  def _insert(self, hash_value, value):
    """
    Insert a given value with its ha
    """
    if self.cache[hash_value] is None:
      self.cache[hash_value] = Node(value)
      return
    curr = self.cache[hash_value]
    while curr.next is not None:
      curr = curr.next
    curr.next = Node(value)

  def insert1(self, value):
    """
    Insert a value into the table

    Division method
    ---------------
    h(k) = k mod size
    Is good if m is prime and not close to 2 ** n or 10 ** n for any n
    """
    hash_value = hash(value) % self.size
    return self._insert(hash_value, value)

  def search1(self, value):
    """
    Division method search
    """
    hash_value = hash(value) % self.size
    return self._search(hash_value, value)

  def insert2(self, value):
    """
    Insert a value into the value
    when size is a power of 2

    Multiplication method
    ---------------------
    h(k) = [(a * k) mod (2 ** 64)] >> (64 - lg(m))
    where a = random int in (lg(m) - 1, m)
    """
    hash_value = (self.mult_constant * value) % (1 << 64)
    hash_value = hash_value >> (64 - self.lg_size)
    return self._insert(hash_value, value)

  def search2(self, value):
    """
    Search using multiplication method
    """
    hash_value = (self.mult_constant * value) % (1 << 64)
    hash_value = hash_value >> (64 - self.lg_size)
    return self._search(hash_value, value)

  def insert3(self, value):
    """
    Insert a value

    Universal method
    ----------------
    h(k) = (((a * k) + b) mod p) mod size
    Where:
      p is a VERY large prime number
      a, b are random ints in [0, p)
    """
    hash_value = (self.univ_a * value) + self.univ_b
    hash_value %= self.large_prime
    hash_value %= self.size
    return self._insert(hash_value, value)

  def search3(self, value):
    """
    Search using universal method
    """
    hash_value = (self.univ_a * value) + self.univ_b
    hash_value %= self.large_prime
    hash_value %= self.size
    return self._search(hash_value, value)
