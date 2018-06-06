"""
Speeding up Djikstra's,
Bi-Directional Shortest Path Search,
Goal Directed Path Search
-------------------------

"""


def single_target_djikstra(adjacency_list, weights, s, t):
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
    if u == t: # terminate early if you find the target
      return (path_costs[t], predecessors)
    for v in adjacency_list[u]:
      if path_costs[u] + weights[(u, v)] < unfinished[v]:
        unfinished[v] = path_costs[u] + weights[(u, v)]
        predecessors[v] = u
  return (path_costs[t], predecessors)


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
        backwards_adjacency_list[v] = set([u])
  return backwards_adjacency_list


def bidirectional_djikstra(adjacency_list, weights, s, t):
  """
  Bi-directional Djikstra's algorithm

  Alternate
  """
  backwards_adjacency_list = construct_backwards_adjacency_list(adjacency_list)
  unfinished_forward = {} # initialize 2 instances of the data structs
  unfinished_backward = {}
  for u in adjacency_list:
    unfinished_forward[u] = float('inf')
    unfinished_backward[u] = float('inf')
  unfinished_forward[s] = 0
  unfinished_backward[t] = 0
  forward_predecessors = {s: None}
  backward_predecessors = {}
  forward_path_costs = {}
  backward_path_costs = {}
  while unfinished_forward or unfinished_backward:
    if unfinished_forward: # forward search step
      u = min(unfinished_forward, key=unfinished_forward.get)
      forward_path_costs[u] = unfinished_forward[u]
      del unfinished_forward[u]
      for v in adjacency_list[u]:
        if forward_path_costs[u] + weights[(u, v)] < unfinished_forward[v]:
          unfinished_forward[v] = forward_path_costs[u] + weights[(u, v)]
          forward_predecessors[v] = u
    if unfinished_backward: # backward search step
      u = min(unfinished_backward, key=unfinished_backward.get)
      backward_path_costs[u] = unfinished_backward[u]
      del unfinished_backward[u]
      for v in backwards_adjacency_list[u]:
        if backward_path_costs[u] + weights[(v, u)] < unfinished_backward[v]:
          unfinished_backward[v] = backward_path_costs[u] + weights[(v, u)]
          backward_predecessors[v] = u
    visited_by_both = set(list(forward_path_costs)).intersection(set(list(backward_path_costs)))
    if visited_by_both: # check if any nodes have been reached by both directions
      joint_costs = {}
      for u in forward_path_costs: # Find the vertex visited by both searches with the min total cost from each
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
      predecessors = {s: None} # Construct the shortest path from s to t
      curr = min_cost_vertex
      while curr != s:
        predecessors[curr] = forward_predecessors[curr]
        curr = forward_predecessors[curr]
      curr = min_cost_vertex
      while curr != t:
        predecessors[backward_predecessors[curr]] = curr
        curr = backward_predecessors[curr]
      return (joint_costs[min_cost_vertex], predecessors)
  return (float('inf'), {})


def goal_directed_djikstra(adjacency_list, weights, s, t, l):
  """
  Djikstra's with an added heuristic that represents
  the "potential" at each vertex

  For this implementation, it is the cost of the shortest
  path from each vertex to a chosen landmark, l

  With a well-chosen l, this can speed up Djikestra's
  for a large graph

  """
  paths_to_landmark = {}
  unfinished = {}
  for u in adjacency_list:
    unfinished[u] = float('inf')
    (cost, _) = single_target_djikstra(adjacency_list, weights, u, l)
    paths_to_landmark[u] = cost
  unfinished[s] = 0
  predecessors = {s: None}
  path_costs = {}
  get_weight = lambda u, v: \
    weights[(u, v)] \
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
  return (path_costs, predecessors)
