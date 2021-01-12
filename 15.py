def count_routes(x, y, memory):
  key = 'x' + str(x) + 'y' + str(y)
  if key in memory:
    return memory[key]
  if (x, y) == (0, 0):
    return 1
  elif x < 0 or y < 0:
    return 0
  else:
    ret_val = count_routes(x-1, y, memory) + count_routes(x, y-1, memory)
    memory[key] = ret_val
    return ret_val
  
memory = {}
print(count_routes(20, 20, memory))