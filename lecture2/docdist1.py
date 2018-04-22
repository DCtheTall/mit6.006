from get_documents import get_documents
import math


def get_words_from_string(line):
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
  word_list = []
  for line in L:
    words_in_line = get_words_from_string(line)
    word_list += words_in_line
  return word_list


def count_frequency(word_list):
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
  word_list = get_words_from_line_list(line_list)
  freq_map = count_frequency(word_list)
  return freq_map


def inner_product(L1, L2):
  result = 0.
  for word1, count1 in L1:
    for word2, count2 in L2:
      if word1 == word2:
        result += count1 * count2
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
