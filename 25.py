bound = 1000
fibs = [None] * 5000
fibs[0] = 1
fibs[1] = 1

counter = 2
while(True):
  newFib = fibs[counter - 1] + fibs[counter - 2]
  if len(str(newFib)) >= bound:
    print(counter + 1)
    break
  fibs[counter] = newFib
  counter += 1