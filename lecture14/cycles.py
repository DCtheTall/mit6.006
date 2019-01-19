"""
Lecture 14: Depth-First Search
------------------------------
This program contains an implementation of
a cycle detection algorithm for directed graphs.
It uses depth-first search to detect if a
graph contains any cycles.

"""


def has_cycle_visit(visiting, parents, adjacency_list, s):
  """
  Check if there is a cycle in a graph starting
  at the node s

  """
  visiting[s] = True
  for u in adjacency_list[s]:
    if u in visiting:
      return True
    if u in parents:
      continue
    parents[u] = s
    if has_cycle_visit(visiting, parents, adjacency_list, u):
      return True
  del visiting[s]
  return False


def has_cycle(adjacency_list):
  """
  Test if a graph that may not
  be strongly connected has any
  cyckes (or any backwards edges)

  """
  visiting = {}
  parents = {}
  for u in adjacency_list:
    if u not in parents:
      parents[u] = None
      if has_cycle_visit(visiting, parents, adjacency_list, u):
        return True
  return False
