import itertools

n = 10
s = ""
for i in range(n):
    s += str(i)

permutations = list(itertools.permutations(s, 3))
checks = [2,3,5,7,11,13,17]
divisible_mapper = {}
for check in checks:
    divisible_mapper[check] = []
for p in permutations:
    number = int("".join(p))
    for check in checks:
        if number % check == 0:
            n_s = str(number)
            if len(n_s) == 2:
                n_s = "0" + n_s
            divisible_mapper[check].append(n_s)

numbers = [str(i) for i in range(10)]
for check in checks:
    if check == 2:
        new_numbers = []
        for number in numbers:
            for c in divisible_mapper[check]:
                new_number = number + c
                new_numbers.append(new_number)
        numbers = new_numbers
    else:
        new_numbers = []
        l = len(numbers[0])
        for number in numbers:
            for p in divisible_mapper[check]:
                p_s = str(p)
                if p_s[0] == number[l-2] and p_s[1] == number[l-1] and p_s[2] not in number:
                    new_number = number + p_s[2]
                    new_numbers.append(new_number)
        numbers = new_numbers
numbers = list(filter(lambda x: len(set(x)) == len(x), numbers))
numbers = list(map(lambda x: int(x), numbers))

print(sum(numbers))