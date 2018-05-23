"""
Shortest paths through a DAG
Djikstra's shortest path algorithm

"""


from lecture14 import topological_sort


def add_directed_weighted_edge(adjacency_list, weights, u, v, w):
  """
  Add a directed edge from vertex u to vertex v
  with weight w

  adjacency_list and weights are both dictionaries
  used for storing graph data

  """
  adjacency_list[u].append(v)
  weights[(u, v)] = w


def shortest_paths_in_dag(adjacency_list, weights, s):
  """
  Return a dictonary with the shortest paths
  to all the nodes

  Weights can be real numbers and this algorithm
  works

  """
  sorted_dag = topological_sort(adjacency_list) # topologically sort the DAG
  path_costs = {}
  predecessors = {}
  for v in sorted_dag: # first mark each node as having an infinite cost to reach
    if v != s:
      path_costs[s] = float('inf')
      predecessors[v] = None
  path_costs[s] = 0 # Then mark the staring node as having cost 0
  for i in range(sorted_dag.index(s), len(sorted_dag)):
    u = sorted_dag[i]
    for v in adjacency_list[u]:
      if path_costs[u] + weights[(u, v)] < path_costs[v]:  # relaxation occurs here
        path_costs[v] = weights[(u, v)]
        predecessors[v] = u
  return (path_costs, predecessors)


def dijkstra(adjacency_list, weights, s):
  """
  Dijkstra's algorithm for finding
  the least cost path to each vertex
  from s given that each edge weight
  is >= 0

  """
  unfinished = dict(adjacency_list)
  unfinished[s] = 0
  for u in unfinished: # create a dict of all unfinished vertices cost from s
    if u != s:
      unfinished[u] = float('inf')
  path_costs = {}
  predecessors = { s: None }
  while unfinished:
    u = min(unfinished) # get the closest vertex to s (starting with s)
    path_costs[u] = unfinished[u]  # record the cost to get there
    del unfinished[u] # remove it from the set of unfinished vertices
    for v in adjacency_list[u]:
      if v in path_costs: # for each unfinished vertex adjacent to u
        continue
      if path_costs[u] + weights[(u, v)] < unfinished[v]: # relax each path
        unfinished[v] = path_costs[u] + weights[(u, v)]
        predecessors[v] = u
  return (path_costs, predecessors)
