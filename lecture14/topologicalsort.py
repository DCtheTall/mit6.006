"""
Lecture 14: Depth-First Search
------------------------------
This program contains an implementation of
topolical sort for a directed, acyclic graph
that uses depth-first search.

"""


def topological_sort_dfs_visit(sorted_list, visiting, parents, adjacency_list, s):
  """
  Visit a node and do a depth
  first search

  If the node is already being visited,
  this implies the existence of a
  backwards edge, which raises an
  exception

  Once visiting the node is finished,
  append it to the list

  """
  visiting[s] = True
  for u in adjacency_list[s]:
    if u in visiting:
      raise Exception
    if u in parents:
      continue
    parents[u] = s
    topological_sort_dfs_visit(
      sorted_list,
      visiting,
      parents,
      adjacency_list,
      u,
    )
  del visiting[s]
  sorted_list.append(s)


def topological_sort(adjacency_list):
  """
  Topological sort on a graph
  using depth first search

  Assumes the graph is a DAG

  Complexity: O(v + e)

  """
  visiting = {}
  parents = {}
  sorted_list = []
  for u in adjacency_list:
    if u not in parents:
      parents[u] = None
      topological_sort_dfs_visit(
        sorted_list,
        visiting,
        parents,
        adjacency_list,
        u,
      )
  sorted_list.reverse()
  return sorted_list
