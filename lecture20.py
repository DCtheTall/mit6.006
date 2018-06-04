"""
Dynamic Programing II:
Text justification

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


def text_justify(page_width, text):
  """
  Justify text on a given page given
  a list of words

  Implementation based on: https://stackoverflow.com/questions/18200593/implementing-text-justification-with-dynamic-programming?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

  """
  words = text.split()
  word_lengths = [len(word) for word in words]
  n = len(words)
  min_badnesses = {0: 0}
  parents = {}
  for i in range(1, n + 1):
    sums = {}
    k = i
    curr_badness = 0
    while k > 0 and curr_badness != float('inf'):
      curr_badness = badness(page_width, word_lengths, k, i) + min_badnesses[k - 1]
      sums[curr_badness] = k
      k -= 1
    min_badnesses[i] = min(sums)
    parents[i] = sums[min(sums)]
  curr = n
  justified_text = []
  while curr > 1:
    justified_text.append(' '.join(words[parents[curr] - 1 : curr]))
    curr = parents[curr]
  justified_text.reverse()
  return '\n'.join(justified_text)

