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


class Node:
  """
  Linked list node

  """
  def __init__(self, value):
    self.value = value
    self.next = None # should be set to another Node


class HashTable:
  """
  Hash table with chaining
  that stores objects in a table with length size (int)

  """
  def __init__(self, size, hash_fn):
    self.size = size
    self.cache = [None for _ in range(size)]
    self.hash_fn = hash_fn

  def _insert(self, hash_value, value):
    """
    Insert a given value with its hash

    """
    if self.cache[hash_value] is None:
      self.cache[hash_value] = Node(value)
      return
    curr = self.cache[hash_value]
    while curr.next is not None:
      curr = curr.next
    curr.next = Node(value)

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

  def insert(self, value):
    """
    Insert a value into the table

    """
    return self._insert(self.hash_fn(value), value)

  def search(self, value):
    """
    Search for a value in the table

    """
    return self._search(self.hash_fn(value), value)


class DivHashTable(HashTable):
  """
  Division method
  ---------------
  h(k) = k mod size
  Is good if m is prime and not close to 2 ** n or 10 ** n for any n

  """
  def __init__(self, size):
    HashTable.__init__(self, size, self.div_hash)

  def div_hash(self, value):
    """
    Hash function implementation

    """
    return hash(value) % self.size


class MultHashTable(HashTable):
  """
  Multiplication method
  ---------------------
  h(k) = [(a * k) mod (2 ** 64)] >> (64 - lg(m))
  where a = random int in (lg(m) - 1, m)

  """
  def __init__(self, size):
    HashTable.__init__(self, size, self.mult_hash)
    self.lg_size = 0
    while size > 1:
      size >>= 1
      self.lg_size += 1
    self.mult_constant = randint(
      (1 << (self.lg_size - 1)) + 1,
      (1 << self.lg_size) - 1,
    )

  def mult_hash(self, value):
    """
    Hash function implementation

    """
    hash_value = (self.mult_constant * value) % (1 << 64)
    hash_value = hash_value >> (64 - self.lg_size)
    return hash_value


class UnivHashTable(HashTable):
  """
  Universal method
  ----------------
  h(k) = (((a * k) + b) mod p) mod size
  Where:
    p is a prime number larger than size
    a, b are random ints in [0, p)

  """
  def __init__(self, size):
    HashTable.__init__(self, size, self.univ_hash)
    self.large_prime = get_larger_prime(2 * self.size)
    self.univ_a = randint(0, self.large_prime - 1)
    self.univ_b = randint(0, self.large_prime - 1)

  def univ_hash(self, value):
    """
    Universal hash function

    """
    hash_value = (self.univ_a * hash(value)) + self.univ_b
    hash_value %= self.large_prime
    hash_value %= self.size
    return hash_value
