def generate_permutations(partial, digits, index, permutations, bound):
  if len(partial) == len(digits):
    permutations.append(partial)
  elif len(permutations) < bound:
      for i in range(len(digits)):
        digit = digits[i]
        if digit not in partial:
          generate_permutations(partial + [digit], digits, i, permutations, bound)

permutations = []
digits = [0,1,2,3,4,5,6,7,8,9]
bound = 1000000
generate_permutations([], digits, 0, permutations, bound)
print("".join([str(c) for c in permutations[bound - 1]]))