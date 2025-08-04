# Algoritmo de ordenacao por bolha
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for x in range(0, n=i-1):
      if arr[x] > arr[x+1]:
        arr[x], arr[x+1] = arr[x+1], arr[x]
  return arr 