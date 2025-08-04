# Algoritmo de agendamento
def fifo_scheduling(processes):
  queue = sorted(processes, key=lambda x: x['arrival'])
  current_time = 0
  for process in queue:
    if current_time < process['arrival']:
      current_time = process['arrival']
    process['start'] = current_time
    current_time += process['burst']
    process['end'] = current_time
  return queue