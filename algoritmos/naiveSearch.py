# Algoritmo de busca padrao
def naive_search(text, pattern):
  for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
      return i
  return -1