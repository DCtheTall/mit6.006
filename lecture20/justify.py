"""
Dynamic Programing II:
======================

Text justification
------------------

"""


def badness(page_width, word_lengths, i, j):
  """
  Get the "badness" of a line of text
  given the width of the page you are
  trying to fit it on

  """
  total_width = sum(word_lengths[i-1:j]) + j - i + 1
  if page_width < total_width:
    return float('inf')
  return (page_width - total_width) ** 3


def justify_text(page_width, text):
  """
  Justify text for a given page width given
  a list of words

  Implementation based on:
  https://stackoverflow.com/questions/18200593/implementing-text-justification-with-dynamic-programming

  Complexity: O(n ** 2)

  """
  words = text.split()
  word_lengths = [len(word) for word in words]
  n = len(words)
  min_badnesses = {0: 0}
  parents = {}
  for i in range(1, n + 1):
    badnesses = {}
    k = i
    curr_badness = 0
    while k > 0 and curr_badness != float('inf'):
      curr_badness = badness(page_width, word_lengths, k, i) + min_badnesses[k - 1]
      badnesses[curr_badness] = k
      k -= 1
    min_badnesses[i] = min(badnesses)
    parents[i] = badnesses[min(badnesses)]
  curr = n
  justified_text = []
  while curr > 1:
    justified_text.append(' '.join(words[parents[curr] - 1 : curr]))
    curr = parents[curr]
  justified_text.reverse()
  return '\n'.join(justified_text)
