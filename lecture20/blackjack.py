"""
Lecture 20: Dynamic Programming
Perfect information Black Jack
------------------------------
This program contains an implementation of an
algorithm to find the "perfect" game of blackjack,
i.e. the game where the player makes as much money
as possible, given that they know the exact order
of the deck.

"""


import random


class Card:
  """
  Card class for Black Jack

  """

  def __init__(self, n):
    self.value = 'ace' if n == 1 else min(n, 10)


def get_shuffled_deck():
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
  curr = start
  curr_hand = list(starting_hand)
  curr_value = get_hand_value(starting_hand)
  hits = 0
  while 0 < curr_value < 17 and curr < (len(deck) - 1):
    curr += 1
    hits += 1
    curr_hand.append(deck[curr])
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
  if (start + hits) >= len(deck):
    return (0, -float('inf'))
  if (start + hits) > (len(deck) - 4):
    return (len(deck) - start, -float('inf'))
  (player_hand, dealer_hand) = deal_hands(deck, start)
  i = 0
  while i < hits and get_hand_value(player_hand) > 0:
    player_hand.append(deck[start + 4 + i])
    i += 1
  cards_played = i + 4
  (dealer_hits, dealer_hand) = play_dealer_turn(
      deck, start + hits + 4, dealer_hand)
  cards_played += dealer_hits
  return (
      cards_played,
      get_game_score(player_hand, dealer_hand),
  )


def perfect_blackjack(deck):
  """
  Perfect information Black Jack

  Given that you know every card in the deck
  this computes the best possible game you
  can play

  Returns 2 dictionaries, one is the most
  the player can win if the deck starts at
  that card, the 2nd is a parent pointer
  which shows how many hits the player
  should take when the deck starts at
  a particular card

  """
  best_scores = {52: -float('inf')}
  best_hits = {}
  for i in range(51, -1, -1):
    scores = {}
    for hits in range(0, 52 - i):
      cards_played, game_score = round_outcome(deck, i, hits)
      if best_scores[i + cards_played] != -float('inf'):
        game_score += best_scores[i + cards_played]
      if game_score not in scores:
        scores[game_score] = hits
    best_scores[i] = max(scores)
    best_hits[i] = scores[max(scores)]
  return best_scores, best_hits
