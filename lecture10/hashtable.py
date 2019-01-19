"""
Lecture 10: Probing
and Cryptographic Hashing
-------------------------
This program contains an implementation of a
has table which uses probing to handle
collisions.

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


class ProbingHashTable:
  """
  A probing hash table which uses double
  hashing to prevent clustering

  Creates a table of size 2^n

  """
  def __init__(self, n):
    self.size = 1 << n
    self.cache = [None for _ in range(self.size)]
    self.large_prime = get_larger_prime(self.size)
    self.univ_a = randint(0, self.large_prime - 1)
    self.univ_b = randint(0, self.large_prime - 1)

  def _univ_hash(self, value):
    """
    Universal hash function
    h(k) = (((a * k) + b) % p) % size

    where p is a prime number at least twice as large as the size
    a, b are random integers between 0 and p - 1

    """
    hash_value = (self.univ_a * hash(value)) + self.univ_b
    hash_value %= self.large_prime
    hash_value %= self.size
    return hash_value

  def _get_hash(self, attempt, value):
    """
    Double hashing implmentation
    h(val, i) = (h(val) + (((2 * h(val)) + 1) * attempted)) mod size

    """
    return (self._univ_hash(value) \
      + ((self._univ_hash(value) << 1) + 1) * attempt) % self.size

  def insert(self, value):
    """
    Insert a value into the table.

    """
    hash_value = self._get_hash(0, value)
    attempt = 0
    while self.cache[hash_value] \
      or self.cache[hash_value] == 0:
        attempt += 1
        hash_value = self._get_hash(attempt, value)
    self.cache[hash_value] = value

  def delete(self, value):
    """
    Delete a value from the table

    To distinguish empty values from
    deleted ones, it replaces them
    with False instead of None.

    """
    hash_value = self._get_hash(0, value)
    attempt = 0
    while self.cache[hash_value] != value \
      or self.cache[hash_value] is not None:
        attempt += 1
        hash_value = self._get_hash(attempt, value)
    if self.cache[hash_value] is None:
      return
    self.cache[hash_value] = False

  def search(self, value):
    """
    Search the hash table for a particular value.

    """
    hash_value = self._get_hash(0, value)
    attempt = 0
    while self.cache[hash_value] != value \
      or self.cache[hash_value] is not None:
        attempt += 1
        hash_value = self._get_hash(attempt, value)
    return self.cache[hash_value] is not None
