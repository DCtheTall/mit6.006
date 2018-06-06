"""
Dynamic Programing II:
Text justification,
Perfect Information Blackjack

"""

import random


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


"""
Perfect information Black Jack

"""


class Card:
  """
  Card class for Black Jack

  """
  def __init__(self, n):
    self.value = 'ace' if n == 1 else min(n, 10)


def build_shuffled_deck():
  """
  Create a shuffled deck of Card instances

  """
  deck = []
  for _ in range(1, 5):
    for i in range(1, 14):
      deck.append(Card(i))
  random.shuffle(deck)
  return deck


def get_hand_value(cards):
  """
  Get the value of a hand of Black Jack cards

  """
  curr_value = 0
  aces = 0
  for card in cards:
    if card.value == 'ace':
      curr_value += 11
      if curr_value > 21:
        curr_value -= 10
      else:
        aces += 1
    else:
      curr_value += card.value
    if curr_value > 21:
      while aces > 0 and curr_value > 21:
        curr_value -= 10
        aces -= 1
      if curr_value > 21:
        return -float('inf')
  return curr_value


def deal_hands(deck, start):
  """
  Deal hands from the deck starting at index i

  """
  return (
    [deck[start], deck[start + 2]],
    [deck[start + 1], deck[start + 3]],
  )


def play_dealer_turn(deck, start, starting_hand):
  """
  Play the dealer's turn starting at index i in the deck
  of cards

  """
  curr_hand = list(starting_hand)
  curr_value = get_hand_value(starting_hand)
  hits = 0
  while 0 < curr_value < 17 and (start + hits) < 52:
    start += 1
    hits += 1
    curr_hand.append(deck[start])
    curr_value = get_hand_value(starting_hand)
  return (hits, curr_hand)


def get_game_score(player_hand, dealer_hand):
  """
  Get the game score

  Returns 1 (played win), 0 (tie), -1 (dealer win)

  """
  player_score = get_hand_value(player_hand)
  dealer_score = get_hand_value(dealer_hand)
  if max(player_score, dealer_score) == player_score:
    return 1
  if player_score == dealer_score:
    return 0
  return -1


def round_outcome(deck, start, hits):
  """
  Determine round outcome

  Returns tuple with number of cards played that
  turn and the result of the game

  """
  (player_hand, dealer_hand) = deal_hands(deck, start)
  for i in range(hits):
    player_hand.append(deck[start + 4 + i])
  cards_played = hits + 4
  (dealer_hits, dealer_hand) = play_dealer_turn(deck, start + hits + 4, dealer_hand)
  cards_played += dealer_hits
  return (cards_played, get_game_score(player_hand, dealer_hand))
