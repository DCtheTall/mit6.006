"""
Lecture 18: Speeding Up Dijkstra's
Bi-Directional Dijkstra's Algorithm
-----------------------------------
This program contains an implementation of
single-target Dijkstra's algorithm which
does a two concurrent searches, one from the
source, one from the vertex, until they are
find a common vertex. Then it finds the miminum
cost bridge between the two subgraphs spanned
by either search to find the shortest path.

"""


def construct_backwards_adjacency_list(adjacency_list):
  """
  Create an adjacency list for traversing a graph
  backwards

  The resulting adjacency dictionary maps
  vertices to each vertex with an edge
  pointing to them

  """
  backwards_adjacency_list = {}
  for u in adjacency_list:
    for v in adjacency_list[u]:
      try:
        backwards_adjacency_list[v].add(u)
      except:
        backwards_adjacency_list[v] = {u}
  return backwards_adjacency_list


def bidirectional_djikstra(adjacency_list, weights, src, dst):
  """
  Bi-directional Djikstra's algorithm.
  It executres Dijkstra's from bothm sides until both searches
  reach a common vertex. It then finds the minimum path connecting
  the two vertices. The proof of this algorithm's correctness
  is covered in lecture.

  """
  backwards_adjacency_list = construct_backwards_adjacency_list(adjacency_list)
  unfinished_forward = dict()  # initialize 2 instances of the data structs
  unfinished_backward = dict()
  for u in adjacency_list:
    unfinished_forward[u] = float('inf')
    unfinished_backward[u] = float('inf')
  unfinished_forward[src] = 0
  unfinished_backward[dst] = 0
  forward_predecessors = {src: None}
  backward_predecessors = dict()
  forward_path_costs = dict()
  backward_path_costs = dict()
  while unfinished_forward or unfinished_backward:
    if unfinished_forward:  # forward search step
      u = min(unfinished_forward, key=unfinished_forward.get)
      forward_path_costs[u] = unfinished_forward[u]
      del unfinished_forward[u]
      for v in adjacency_list[u]:
        if forward_path_costs[u] + weights[(u, v)] < unfinished_forward[v]:
          unfinished_forward[v] = forward_path_costs[u] + weights[(u, v)]
          forward_predecessors[v] = u
    if unfinished_backward:  # backward search step
      u = min(unfinished_backward, key=unfinished_backward.get)
      backward_path_costs[u] = unfinished_backward[u]
      del unfinished_backward[u]
      for v in backwards_adjacency_list[u]:
        if backward_path_costs[u] + weights[(v, u)] < unfinished_backward[v]:
          unfinished_backward[v] = backward_path_costs[u] + weights[(v, u)]
          backward_predecessors[v] = u
    visited_by_both = {c for c in forward_path_costs}.intersection(
        {c for c in backward_path_costs})
    if visited_by_both:  # check if any nodes have been reached by both directions
      joint_costs = dict()
      for u in forward_path_costs:  # Find the vertex visited by both searches with the min total cost from each
        joint_costs[u] = forward_path_costs[u]
        if u in backward_path_costs:
          joint_costs[u] += backward_path_costs[u]
        else:
          joint_costs[u] += unfinished_backward[u]
      for u in backward_path_costs:
        if u in forward_path_costs:
          continue
        joint_costs[u] = backward_path_costs[u] + unfinished_forward[u]
      min_cost_vertex = min(joint_costs, key=joint_costs.get)
      predecessors = {src: None}  # Construct the shortest path from s to t
      cur = min_cost_vertex
      while cur != src:
        predecessors[cur] = forward_predecessors[cur]
        cur = forward_predecessors[cur]
      cur = min_cost_vertex
      while cur != dst:
        predecessors[backward_predecessors[cur]] = cur
        cur = backward_predecessors[cur]
      return (joint_costs[min_cost_vertex], predecessors)
  return float('inf'), dict()
