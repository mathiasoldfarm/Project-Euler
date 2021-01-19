import sys

with open('data/names.txt') as f:
  content = f.read()
content = content.replace('"', '').strip().split(",")
content.sort()
print(content)

alphabet_string = "abcdefghijklmnopqrstuvwxyz"
alphabet = {}
counter = 1
for letter in alphabet_string:
  alphabet[letter] = counter
  counter += 1

def get_worth(word, index):
  s = 0
  for c in word:
    s += alphabet[c.lower()]
  return s * index

print(sum([ get_worth(content[i], i+1) for i in range(len(content))]))