triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

lines = triangle.split("\n")
for i in range(len(lines)):
  line = lines[i]
  line = line.split(" ")
  line = list(map(lambda x: int(x), line))
  lines[i] = line

def get_largest_sum(triangle, line_index, path_index, memory):
  key = f"l{line_index}p{path_index}"
  if key in memory:
    return memory[key]
  if line_index == len(triangle) - 1:
    return triangle[line_index][path_index]
  else:
    if path_index >= len(triangle[line_index]):
      res = triangle[line_index][path_index] + get_largest_sum(triangle, line_index + 1, path_index, memory)
    else:
      res = triangle[line_index][path_index] + max(
        get_largest_sum(triangle, line_index + 1, path_index, memory),
        get_largest_sum(triangle, line_index + 1, path_index + 1, memory)
      )
    memory[key] = res
    return res

memory = {}
s = get_largest_sum(lines, 0, 0, memory)
print(s)