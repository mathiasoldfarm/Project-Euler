def count_sequence(n, memory):
  if n in memory:
    return memory[n]
  if n == 1:
    ret_val = 1
  elif n % 2 == 0:
    ret_val = 1 + count_sequence(n / 2, memory)
  else:
    ret_val = 1 + count_sequence(3 * n + 1, memory)

  memory[n] = ret_val
  
  return ret_val

max_length = 0
max_length_start = None
bound = 1000000
memory = {}
for i in range(1,bound):
  if i not in memory:
    sequence_length = count_sequence(i, memory)
    if sequence_length > max_length:
      max_length = sequence_length
      max_length_start = i

print(max_length, max_length_start)