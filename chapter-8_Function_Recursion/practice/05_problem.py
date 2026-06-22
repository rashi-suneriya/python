#  write a py fucn to remove a given word from a list ad strip it at the same

def rem(l, word):
  n = []
  for item in l:
    if not(item == word):
      n.append(item.strip(word))
  return n
  
  
l = ["Harry", "Rohan", "subhham", "an"]

print(rem(l, "an"))



#  write a py fucn to print multiplication table of a given number.

def multiply(n):
  for i in range(1, 11):
    print(f"{n}X {i} = {n*i}")
    
multiply(5)