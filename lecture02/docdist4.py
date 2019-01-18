"""
Lecture 2:
Document Distance
-----------------
This iteration improves the document distance
algorithm by using a hash map to compute the
frequency vectors for each document.

"""


from get_documents import get_documents
import math


def get_words_from_string(line):
  """
  Split a string into a list of words.

  """
  word_list = []
  char_list = []
  for c in line:
    if c.isalnum():
      char_list.append(c)
    elif len(char_list) > 0:
      word = ''.join(char_list).lower()
      word_list.append(word)
      char_list = []
  if len(char_list) > 0:
    word = ''.join(char_list).lower()
    word_list.append(word)
  return word_list


def get_words_from_line_list(L):
  """
  Transform the lines in the document, a list
  of strings, into a list of words.

  """
  word_list = []
  for line in L:
    words_in_line = get_words_from_string(line)
    word_list.extend(words_in_line)
  return word_list


def count_frequency(word_list):
  """
  Count the frequency of each word in the list
  by scanning the list of already encountered
  words.

  """
  D = dict()
  for new_word in word_list:
    if new_word in D:
      D[new_word] = D[new_word] + 1
    else:
      D[new_word] = 1
  return D.items()


def insertion_sort(L):
  """
  Insertion sort, a list sorting
  algorithm.

  """
  for i in range(len(L)):
    key = L[i]
    j = i - 1
    while j > -1 and L[j] > key:
      L[j + 1] = L[j]
      j -= 1
    L[j + 1] = key
  return L


def word_frequencies_for_file(line_list):
  """
  Transform the document into a frequency map
  for each term.

  """
  word_list = get_words_from_line_list(line_list)
  freq_map = count_frequency(word_list)
  insertion_sort(freq_map)
  return freq_map


def inner_product(L1, L2):
  """
  Take the inner product of the frequency maps.

  """
  result = 0.
  i = 0
  j = 0
  while i < len(L1) and j < len(L2):
    if L1[i][0] == L2[j][0]:
      result += L1[i][1] * L2[j][1]
      i += 1
      j += 1
    elif L1[i][0] < L2[j][0]:
      i += 1
    else:
      j += 1
  return result


def vector_angle(L1, L2):
  """
  Compute the angle between two frequency vectors.

  """
  numerator = inner_product(L1, L2)
  denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
  return math.acos(numerator / denominator)


def main():
  """
  Compute the document distance.

  """
  doc1, doc2 = get_documents()
  freq_map1 = word_frequencies_for_file(doc1)
  freq_map2 = word_frequencies_for_file(doc2)
  distance = vector_angle(freq_map1, freq_map2)
  print 'The distance between the documents is %0.6f (radians)' % distance
