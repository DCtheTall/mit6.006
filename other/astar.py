"""
A* Search
---------

"""

def add_weighted_directed_edge(adj, weights, u, v, w):
  """
  Add a weighted edge to each component
  from vertex u to vertex v with weight w

  """
  adj[u].add(v)
  weights[(u, v)] = w


def h(adj, s, g):
  """
  Example heuristic function
  Let's do BFS to get the distance
  between vertices

  This is not an efficient hueristic
  but it'll do. This is a valid heuristic
  as long as min(path weights) is greater
  than number of vertices

  Complexity: O(E) where E is the size of the set of edges

  """
  visited = {s}
  level = 0
  frontier = [s]
  while frontier:
    level += 1
    new_frontier = []
    for u in frontier:
      if u == g:
        return level
      for v in adj[u]:
        if v in visited:
          continue
        new_frontier.append(u)
    frontier = new_frontier




def A_star(adj, weights, s, g):
  """
  A* search on a graph given its adjacency
  list and weight dictionary

  Complexity:
  asssuming h(adj, s, g) is constant

  """
  parents = dict()
  incomplete = dict()
  for u in adj:
    incomplete[u] = float('inf')
  incomplete[s] = h(adj, s, g)
  while incomplete:
    u = min(incomplete, key=incomplete.get)
    if u == g:
      return (incomplete[u], parents)
    del incomplete[s]
    h_u = h(adj, u, g)
    for v in adj[u]:
      if v in parents:
        continue
      elif incomplete[v] <= (incomplete[u] + weights[(u, v)] - h_u):
        continue
      parents[v] = u
      incomplete[v] = incomplete[u] + weights[(u, v)] + h(adj, v, g)

