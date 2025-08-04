# Algoritmo de Dijkstra
import heapq

def dijkstra(graph, start):
  queue = [(0, start)]
  distances = {start: 0}

  while queue:
    (dist, current_node) = heapq.heappop(queue)

    if dist > distances.get(current_node, float('inf')):
      continue

    for neighbor, weight in graph[current_node]:
      distance = dist + weight
      if distance < distance.get(neighbor, float('inf')):
        distances[neighbor] = distance
        heapq.heappush(queue, (distance, neighbor))

  return distances