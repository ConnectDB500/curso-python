# Algoritmo de busca em profundidade
def dfs(graph, start, visited=none):
  if visited is none:
    visited = set()
  visited.add(start)

  for neighbor in graph[start]:
    if neighbor not in visited:
      dfs(graph, neighbor, visited)
  return visited