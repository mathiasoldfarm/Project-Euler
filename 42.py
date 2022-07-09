with open('./Data/words.txt', 'r') as f:
    words = f.read()

words = words.replace("\"", "")
words = words.split(",")

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

mapper = {}
for i, letter in enumerate(alphabet):
    mapper[letter] = i+1

def word_value(word):
    return sum([mapper[letter] for letter in word])

first_triangle_numbers = set()
bound = 200
for i in range(1,1+bound):
    first_triangle_numbers.add(0.5*i*(i+1))

def is_triangle_word(word):
    val = word_value(word)
    if val > bound:
        raise Exception("Bound unexpectedly exceeded")
    return val in first_triangle_numbers

print(sum([1 if is_triangle_word(word) else 0 for word in words]))