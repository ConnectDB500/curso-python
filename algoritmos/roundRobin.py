# Algoritmo de agendamento
def round_robin(processes, quantum):
  queue = processes[:]
  current_time = 0
  result = []
  while queue:
    process = queue.pop(0)
    if process['burst'] > quantum:
      result.append({**process, 'executed': quantum, 'start': current_time})
      current_time += quantum
      process['burst'] -= quantum
      queue.append(process)
    else: 
      result.append({**process, 'executed': process['burst'], 'start': current_time})
      current_time += process['burst']
      process['burst'] = 0
  return result 