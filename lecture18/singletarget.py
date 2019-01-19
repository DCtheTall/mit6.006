"""
Lecture 18: Speeding Up Dijkstra's
Single-Targer Dijkstra's Algorithm
----------------------------------
This program contains an implementation of
Dijkstra's algorithm which halts when it finds
the shortest path to a given destination vertex.
It then returns the path to that vertex from
the source vertex and the cost of the trip.

"""


def single_target_dijkstra(adjacency_list, weights, s, t):
  """
  Single target Djikstra's will terminate once
  a path is found from the source s to target t

  It is the same worst-case complexity but can
  be faster than normal Djikstra's

  """
  unfinished = {}
  for u in adjacency_list:
    unfinished[u] = float('inf')
  unfinished[s] = 0
  predecessors = {s: None}
  path_costs = {}
  while unfinished:
    u = min(unfinished, key=unfinished.get)
    path_costs[u] = unfinished[u]
    del unfinished[u]
    if u == t:  # terminate early if you find the target
      return path_costs[t], predecessors
    for v in adjacency_list[u]:
      if path_costs[u] + weights[(u, v)] < unfinished[v]:
        unfinished[v] = path_costs[u] + weights[(u, v)]
        predecessors[v] = u
  return path_costs[t], predecessors
