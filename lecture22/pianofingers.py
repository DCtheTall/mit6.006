"""
Dynamic Programming IV
======================

1. Piano Fingers

Given a set of rules which determine the cost of
certain piano transactions, what is the optimal
sequence to play a simple sequence of notes

"""


STRETCH_TABLE = {  # source: http://www.diva-portal.org/smash/get/diva2:768564/FULLTEXT01.pdf
  (1, 2): (-5, -3, 1, 5, 8, 10), # tuple represents min range, min comf range, min relaxed range, max relaxed range, max comf range, max range
  (1, 3): (-4, -2, 3, 7, 10, 12),
  (1, 4): (-3, -1, 5, 9, 12, 14),
  (1, 5): (-1, 1, 7, 10, 13, 15),
  (2, 3): (1, 1, 1, 2, 3, 5),
  (2, 4): (1, 1, 3, 4, 5, 7),
  (2, 5): (2, 2, 5, 6, 8, 10),
  (3, 4): (1, 1, 1, 2, 2, 4),
  (3, 5): (1, 1, 3, 4, 5, 7),
  (4, 5): (1, 1, 1, 2, 3, 6),
}

def get_key_color(key):
  """
  Get the color of the piano key
  where the keys are ints in [0, 36]

  """
  return 'black' if (key % 12) in (1, 3, 6, 8, 10) else 'white'

def get_transition_cost(note1, note2, finger1, finger2):
  """
  Get the cost of moving from note1 to note2 (integers)
  when finger1 is already playing note1

  Source: http://www.diva-portal.org/smash/get/diva2:768564/FULLTEXT01.pdf

  I used all of the rules which apply to 2 notes,
  though it is possible to code the rules for 3 I
  did not in the interest of time.

  """
  transition = note2 - note1
  stretches = STRETCH_TABLE[(finger1, finger2)]
  cost = 0
  if transition < stretches[0] or transition > stretches[5]:
    return float('inf')
  if transition < stretches[1]:
    cost += 2 * (stretches[1] - transition)
  if transition > stretches[4]:
    cost += 2 * (transition - stretches[4])
  if transition < stretches[2]:
    cost += stretches[2] - transition
  if transition > stretches[3]:
    cost += (1 if finger1 == 1 else 2) * (transition - stretches[3])
  if finger1 in (4, 5):
    cost += 1
  if finger2 in (4, 5):
    cost += 1
  if len({finger1, finger2}.intersection({3, 4, 5})) == 2:
    cost += 1
  if finger1 == 3 and finger2 == 4:
    cost += 1
  if {finger1, finger2} == {3, 4} \
    and get_key_color(note1) != get_key_color(note2):
      cost += 1
  if note1 < note2 and finger1 == 1:
    cost += 1 if get_key_color(note1) == get_key_color(note2) \
      else (3 if get_key_color(note1) == 'black' and finger1 == 1 else 0)
  return cost


def get_optimal_fingering(song):
  """
  Get the optimal fingering for a song of single
  notes represented by a list of keys

  """
  pass
