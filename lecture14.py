"""
Depth first search,
backwards edge (cycle) detection,
and topological sort
--------------------

"""


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
  parents = {}
  for u in adjacency_list:
    if u not in parents:
      parents[u] = None
      dfs_visit(parents, adjacency_list, u)


"""
Detecting if a graph has cycles using
the DFS implemntation above

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


"""
Topological sort

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
