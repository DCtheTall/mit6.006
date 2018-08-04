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
  open_set = {s}
  closed_set = set()
  parents = dict()
  g_scores = dict()
  f_scores = dict()
  for u in adj:
    f_scores[u] = float('inf')
    g_scores[u] = float('inf')
  f_scores[s] = h(adj, s, g)
  g_scores[s] = 0
  while open_set:
    u = min(open_set, key=f_scores.get)
    if u == g:
      return (f_scores[u], parents)
    open_set.remove(u)
    closed_set.add(u)
    for v in adj[u]:
      if v in closed_set:
        continue
      elif g_scores[v] <= g_scores[u] + weights[(u, v)]:
        continue
      g_scores[v] = g_scores[u] + weights[(u, v)]
      f_scores[v] = g_scores[v] + h(adj, v, g)

