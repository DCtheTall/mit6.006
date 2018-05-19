"""
Depth first search
and topological sort
--------------------

"""


def non_recursive_bst_dfs(tree, value):
  """
  A recursive depth first search
  on a binary search tree was
  already implemented in lecture5.py

  This implementation uses a stack
  instead of recursion

  Complexity: O(v + e)
  where v is the number of nodes
  and e is the number of edges
  """
  stack = [tree]
  while stack:
    curr = stack.pop()
    if curr.value == value:
      return True
    if value < curr.value and curr.left:
      stack.append(curr.left)
    if value > curr.value and curr.right:
      stack.append(curr.right)
  return False


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

def counting_dfs_visit(op_counts, prev_count, parents, adjacency_list, s):
  count = 0
  for u in adjacency_list[s]:
    if u not in parents:
      parents[u] = s
      count += 1 + counting_dfs_visit(
        op_counts,
        prev_count + count,
        parents,
        adjacency_list,
        u,
      )
  op_counts[s] = prev_count + count
  return count


def topological_sort(adjacency_list):
  op_counts = {}
  parents = {}
  for u in adjacency_list:
    if u not in parents:
      parents[u] = None
      counting_dfs_visit(
        op_counts,
        0,
        parents,
        adjacency_list,
        u,
      )
  result = list(op_counts)
  result.sort(key=lambda node: op_counts[node])
  result.reverse()
  return result
