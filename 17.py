def get_ones(n):
  if n == 1 or n == 2 or n == 6:
    return 3
  if n == 3 or n == 7 or n == 8:
    return 5
  if n == 4 or n == 5 or n == 9:
    return 4

def get_tens(n):
  if n == 10:
    return 3
  if n == 11 or n == 12:
    return 6
  end = 4
  first = n // 10
  last = n % 10
  if n < 20:
    if last == 3 or last == 8:
      return 4 + end
    if last == 5:
      return 3 + end
    if n == 10:
      return 3
    return get_ones(n % 10) + end
  end = 2
  last = get_ones(n % 10)
  if last:
    end += last
  if first == 2 or first == 3 or first == 8:
    return 4 + end
  if first == 5 or first == 4:
    return 3 + end
  return get_ones(first) + end


def get_len(i):
  if i < 100:
    if i < 10:
      return get_ones(i)
    else:
      return get_tens(i)
  else:
    s = 0
    numb = str(i)
    assert(len(numb) == 3)
    s += get_ones(int(numb[0]))
    s += len("hundred")
    end = int(numb[1:])
    if end > 0:
      s += len("and")
      if end < 10:
        s += get_ones(end)
      else:
        s += get_tens(end)
    return s

s = len("onethousand")
for i in range(1,1000):
  s += get_len(i)

print(s)


  