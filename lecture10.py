"""
Probing and cryptographic hashing
---------------------------------

"""

from random import randint
from lecture8 import get_larger_prime


class ProbingHashTable:
  """
  A probing hash table which uses double
  hashing to prevent clustering

  Creates a table of size 2^size

  """
  def __init__(self, size):
    self.size = 1 << size
    self.cache = [None for _ in range(size)]
    self.large_prime = get_larger_prime(1 << size)
    self.univ_a = randint(0, self.large_prime - 1)
    self.univ_b = randint(0, self.large_prime - 1)

  def _univ_hash(self, value):
    """
    Universal hash function

    """
    hash_value = (self.univ_a * hash(value)) + self.univ_b
    hash_value %= self.large_prime
    hash_value %= self.size
    return hash_value

  def _get_hash(self, attempt, value):
    """
    Double hashing implmentation

    """
    return (self._univ_hash(value) \
      + ((self._univ_hash(value) << 1) + 1) * attempt) % self.size

  def insert(self, value):
    """
    Insert a value into the table

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
    with False instead of None

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
    Search the hash table for a particular value

    """
    hash_value = self._get_hash(0, value)
    attempt = 0
    while self.cache[hash_value] != value \
      or self.cache[hash_value] is not None:
        attempt += 1
        hash_value = self._get_hash(attempt, value)
    return self.cache[hash_value] is not None




