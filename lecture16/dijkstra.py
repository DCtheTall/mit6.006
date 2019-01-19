"""
Lecture 16: Single-Source Shortest Path
Dijkstra's Algorithm
--------------------
This program contains an implementation of Dijkstra's
algorithm for finding the shortest path in a directed
graph with non-negative edge weights.

"""


def dijkstra(adjacency_list, weights, s):
  """
  Dijkstra's algorithm for finding
  the least cost path to each vertex
  from s given that each edge weight
  is >= 0

  Complexity:
  Depends on the efficiency of the priority queue
  you use to find the next minimum vertex. This
  implementation is O(v ** 2 + e) but some priority
  queues can achieve O(v * log(v) + e) time.*

  *: where v is the number of vertices in the graph
  and e is the number of edges.

  """
  unfinished = dict()
  for u in adjacency_list:  # create a dict of all unfinished vertices cost from s
    unfinished[u] = float('inf')
  unfinished[s] = 0
  path_costs = dict()
  predecessors = {s: None}
  while unfinished:
    # get the closest vertex to s (starting with s)
    u = min(unfinished, key=unfinished.get)
    path_costs[u] = unfinished[u]  # record the cost to get there
    del unfinished[u]  # remove it from the set of unfinished vertices
    for v in adjacency_list[u]:
      if v in path_costs:  # for each unfinished vertex adjacent to u
        continue
      if path_costs[u] + weights[(u, v)] < unfinished[v]:  # relax each path
        unfinished[v] = path_costs[u] + weights[(u, v)]
        predecessors[v] = u
  return path_costs, predecessors
