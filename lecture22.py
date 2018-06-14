"""
Dynamic Programming IV
======================

Piano Fingering

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


def get_transition_cost(note1, note2, f, g):
  """
  Get the cost of moving from note1 to note2 (integers)
  when finger1 is already playing note1

  Source: http://www.diva-portal.org/smash/get/diva2:768564/FULLTEXT01.pdf

  I used all of the rules which apply to 2 notes,
  though it is possible to code the rules for 3 I
  did not in the interest of time.

  """
  finger1 = min(f, g)
  finger2 = max(f, g)
  transition = note2 - note1
  stretches = STRETCH_TABLE[(finger1, finger2)]
  cost = 0
  if transition < stretches[0]:
    cost += 3 * (stretches[0] - transition)
  if transition > stretches[5]:
    cost += 3 * (transition - stretches[5])
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

  Given the cost model (which admittedly is probably not great)
  this will find the optimal fingering. It's assumed that
  playing the same note twice with the same finger has zero
  cost

  Complexity: O(n)

  """
  optimal_costs = {}
  optimal_fingering = {}
  n = len(song)
  for i in range(n - 1, -1, -1):
    for f in range(1, 6):
      if i == n - 1:
        optimal_costs[(i, f)] = 1 if f in (4, 5) else 0
        optimal_fingering[(i, f)] = (f,)
      else:
        costs = {}
        for g in range(1, 6):
          if f == g:
            if song[i] == song[i + 1]:
              costs[0] = g
              continue
            else:
              continue
          cost = get_transition_cost(song[i], song[i + 1], f, g) \
            + optimal_costs[(i + 1, g)]
          if cost not in costs:
            costs[cost] = g
        best_cost = min(costs)
        optimal_costs[(i, f)] = best_cost
        next_finger = costs[best_cost]
        optimal_fingering[(i, f)] = (f,) + optimal_fingering[(i + 1, next_finger)]
  starting_finger = None
  min_cost = float('inf')
  for f in range(1, 6):
    if optimal_costs[(0, f)] < min_cost:
      starting_finger = f
      min_cost = optimal_costs[(0, f)]
  return (optimal_costs[(0, starting_finger)], optimal_fingering[(0, starting_finger)])
