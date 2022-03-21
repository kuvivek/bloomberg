#! /usr/bin/python3
def non_repeatingchars(str1):
  dict1 = {}
  characters = list(str1)

  for elem in characters:
    if elem not in dict1:
      dict1.setdefault(elem,1)
    else:
      dict1[elem] += 1
  for idx in range(len(characters)):
    if characters[idx] in dict1 and dict1[characters[idx]] == 1:
      return characters[idx]

StringInput = input()
print(non_repeatingchars(StringInput))
