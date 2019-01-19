"""
Lecture 18: Speeding Up Dijkstra's
Goal Directed Dijkstra's Algorithm
----------------------------------
This program contains an implementation of goal-directed
Dijkstra's shortest path graph algorithm. It chooses a point
to be a "landmark" between the source and destination vertex,
and uses the shortest distance from the landmark to each
vertex as a heuristic for a single-target search from a
source vertex to a destination vertex.

The implementation here could be improved by caching the results
from the search starting at the landmark vertex if the landmark
is useful for multiple searches.

"""


from singletarget import single_target_dijkstra


def goal_directed_djikstra(adjacency_list, weights, src, dst, lmrk):
  """
  Dijkstra's with an added heuristic that represents
  the "potential" at each vertex

  For this implementation, it is the cost of the shortest
  path from each vertex to a chosen landmark, lmrk

  With a well-chosen lmrk, this can speed up Dijkstra's
  for a large graph.

  """
  paths_to_landmark = dict()
  unfinished = dict()
  for u in adjacency_list:
    unfinished[u] = float('inf')
    cost, _ = single_target_dijkstra(adjacency_list, weights, u, lmrk)
    paths_to_landmark[u] = cost
  unfinished[src] = 0
  predecessors = {src: None}
  path_costs = dict()
  get_weight = lambda u, v: weights[(u, v)] \
      - paths_to_landmark[u] \
      + paths_to_landmark[v]
  while unfinished:
    u = min(unfinished, key=unfinished.get)
    path_costs[u] = unfinished[u]
    del unfinished[u]
    for v in adjacency_list[u]:
      if path_costs[u] + get_weight(u, v) < unfinished[v]:
        unfinished[v] = path_costs[u] + get_weight(u, v)
        predecessors[v] = u
  return path_costs, predecessors
