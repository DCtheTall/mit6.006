from get_documents import get_documents
import math
import string

translation_table = string.maketrans(
    string.punctuation + string.uppercase,
    " " * len(string.punctuation) + string.lowercase
)


def get_words_from_string(line):
  line = line.encode('utf-8')
  line = line.translate(translation_table)
  word_list = line.split()
  return word_list


def get_words_from_line_list(L):
  word_list = []
  for line in L:
    words_in_line = get_words_from_string(line)
    word_list.extend(words_in_line)
  return word_list


def count_frequency(word_list): # This function now just returns a dictionary
  D = {}
  for new_word in word_list:
    if new_word in D:
      D[new_word] = D[new_word] + 1
    else:
      D[new_word] = 1
  return D


def word_frequencies_for_file(line_list): # This eliminates the need to sort words
  word_list = get_words_from_line_list(line_list)
  freq_map = count_frequency(word_list)
  return freq_map


def inner_product(D1, D2): # Refactored to use dictionaries, much faster
  result = 0.
  for key in D1:
    if key in D2:
      result += D1[key] * D2[key]
  return result


def vector_angle(D1, D2):
  numerator = inner_product(D1, D2)
  denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))
  return math.acos(numerator / denominator)


def main():
  (doc1, doc2) = get_documents()
  freq_map1 = word_frequencies_for_file(doc1)
  freq_map2 = word_frequencies_for_file(doc2)
  distance = vector_angle(freq_map1, freq_map2)
  print 'The distance between the documents is %0.6f (radians)' % distance


main()
