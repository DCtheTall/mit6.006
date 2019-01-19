"""
Lecture 16: Single-Source Shortest Path
Topological Sort Method
-----------------------
This program contains an implementation of an algorithm
for finding the shortest paths to each vertex in the
graph from a given source vertex. This algorithm is
for directed, acyclic graphs, otherwise topological
sort will fail.

"""


def add_directed_weighted_edge(adjacency_list, weights, u, v, w):
  """
  Add a directed edge from vertex u to vertex v
  with weight w

  adjacency_list and weights are both dictionaries
  used for storing graph data

  """
  adjacency_list[u].add(v)
  weights[(u, v)] = w


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


def shortest_paths_in_dag(adjacency_list, weights, s):
  """
  Return a dictonary with the shortest paths
  to all the nodes

  Weights can be real numbers and this algorithm
  works

  """
  sorted_dag = topological_sort(adjacency_list)  # topologically sort the DAG
  path_costs = {}
  predecessors = {}
  for v in sorted_dag:  # first mark each node as having an infinite cost to reach
    if v != s:
      path_costs[s] = float('inf')
      predecessors[v] = None
  path_costs[s] = 0  # Then mark the staring node as having cost 0
  for i in range(sorted_dag.index(s), len(sorted_dag)):
    u = sorted_dag[i]
    for v in adjacency_list[u]:
      if path_costs[u] + weights[(u, v)] < path_costs[v]:  # relaxation occurs here
        path_costs[v] = weights[(u, v)]
        predecessors[v] = u
  return (path_costs, predecessors)
