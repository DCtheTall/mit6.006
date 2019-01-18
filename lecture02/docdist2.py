"""
Lecture 2:
Document Distance
-----------------
This program improves on the first iteration by replacing
list concatenation with the .extend() method, which is more
efficient.

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
    word_list.extend(words_in_line) # Improvement here, .extend is faster than +
  return word_list


def count_frequency(word_list):
  """
  Count the frequency of each word in the list
  by scanning the list of already encountered
  words.

  """
  L = []
  for new_word in word_list:
    for entry in L:
      if new_word == entry[0]:
        entry[1] = entry[1] + 1
        break
    else:
      L.append([new_word, 1])
  return L


def word_frequencies_for_file(line_list):
  """
  Transform the document into a frequency map
  for each term.

  """
  word_list = get_words_from_line_list(line_list)
  freq_map = count_frequency(word_list)
  return freq_map


def inner_product(L1, L2):
  """
  Take the inner product of the frequency maps.

  """
  result = 0.
  for word1, count1 in L1:
    for word2, count2 in L2:
      if word1 == word2:
        result += count1 * count2
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
