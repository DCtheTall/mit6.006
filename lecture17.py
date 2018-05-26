"""
Bellman-Ford algorithm
----------------------

"""


def bellman_ford(adjaceny_list, weights, s):
  """
  Bellman-Ford finds the shortest path to
  each vertex from s in a graph
  which may have negative cycles

  If it detects a negative cycle, it
  will raise an Exception

  Complexity: O(v * e)

  """
  predecessors = {}
  path_costs = {}
  for v in adjaceny_list:
    predecessors[v] = None
    path_costs[v] = float('inf')
  path_costs[s] = 0
  for _ in range(1, len(adjaceny_list)):
    for edge in weights:
      (u, v) = edge
      if path_costs[u] + weights[edge] < path_costs[v]:
        path_costs[v] = path_costs[u] + weights[edge]
        predecessors[v] = u
  for edge in weights:
    if path_costs[u] + weights[edge] < path_costs[v]:
      raise Exception
  return (path_costs, predecessors)

