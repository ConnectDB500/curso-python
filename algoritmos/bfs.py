# Algoritmo de busca em largura
from collections import deque

def bfs(graph, start):
  visited = set()
  queue = deque([start])

  while queue:
    node = queue.popleft()
    if node not in visited:
      visited.add(node)
      for neighbor in graph[node]:
        queue.append(neighbor)
  return visited