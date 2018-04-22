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


def count_frequency(word_list):
  D = {}
  for new_word in word_list:
    if new_word in D:
      D[new_word] = D[new_word] + 1
    else:
      D[new_word] = 1
  return D.items()


def merge(left, right): # merge two ordered lists into a single ordered list
  i = 0
  j = 0
  result = []
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  if i < len(left):
    result.extend(left[i:])
  if j < len(right):
    result.extend(right[j:])
  return result


def merge_sort(L): # merge sort
  n = len(L)
  if n < 2:
    return L
  left = merge_sort(L[:n / 2])
  right = merge_sort(L[n / 2:])
  return merge(left, right)


def word_frequencies_for_file(line_list):
  word_list = get_words_from_line_list(line_list)
  freq_map = count_frequency(word_list)
  freq_map = merge_sort(freq_map) # insertion sort is replaced with more efficient merge sort
  return freq_map


def inner_product(L1, L2):
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
  numerator = inner_product(L1, L2)
  denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
  return math.acos(numerator / denominator)


def main():
  (doc1, doc2) = get_documents()
  freq_map1 = word_frequencies_for_file(doc1)
  freq_map2 = word_frequencies_for_file(doc2)
  distance = vector_angle(freq_map1, freq_map2)
  print 'The distance between the documents is %0.6f (radians)' % distance


main()
