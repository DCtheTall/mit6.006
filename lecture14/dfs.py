"""
Lecture 14: Depth-First Search
------------------------------
This program contains an implementation of
a recursive depth-first search and depth-first
search using a stack.

"""


from collections import deque


def dfs_visit(parents, adjacency_list, s):
  """
  Recursive depth first search for
  the graph data structure implemented
  in lecture13.py which visits all
  nodes connected to s

  """
  for u in adjacency_list[s]:
    if u not in parents:
      parents[u] = s
      dfs_visit(parents, adjacency_list, u)


def dfs(adjacency_list):
  """
  Recursively search the graph
  for all nodes, even if the
  graph is not strongly
  connected

  """
  parents = dict()
  for u in adjacency_list:
    if u not in parents:
      parents[u] = None
      dfs_visit(parents, adjacency_list, u)
  return parents


def stack_dfs(adjacency_list, s):
  """
  DFS using a stack instead of
  recursion

  Complexity: O(v + e)

  """
  parents = dict()
  stack = deque()
  stack.append((None, s))
  while len(stack) > 0:
    parent, u = stack.pop()
    if u in parents:
      continue
    parents[u] = parent
    for v in adjacency_list[u]:
      stack.append((u, v))
  return parents
