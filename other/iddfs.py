"""
Iterated-Depth Depth First Search
aka IDDFS
---------

"""

def dls_visit(
  s,
  adjacency_list,
  depth,
  max_depth,
  parents,
):
  """
  DFS visit checking depth

  """
  if depth == max_depth:
    return
  for u in adjacency_list[s]:
    if u in parents:
      continue
    parents[u] = s
    dls_visit(
      u,
      adjacency_list,
      depth + 1,
      max_depth,
      parents,
    )

def IDDFS(s, g, adjacency_list):
  """
  Iterated-Depth DFS

  Complexity: O(b ** d)

  Where d is the depth of the goal vertex (g)
  from the source vertex (s)
  and b is the graph's branching factor

  Returns a tuple with the depth of the
  goal vertex and parent pointers for the
  graph from s to g (may also contain others)

  """
  depth = 0
  prev = None
  while True:
    depth += 1
    parents = {s: None}
    dls_visit(
        s, adjacency_list, 0, depth, parents)
    if g in parents:
      return (depth, parents)
    if prev == parents:
      return None
    prev = parents

