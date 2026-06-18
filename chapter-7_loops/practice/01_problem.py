# write a prog print multiplication table of given no.

n = int(input("Enter a number: "))

for i in range(1, 11):
  print(f"{n} X {i} = {n * i}")
  
  #  solve in while loop
  
n = int(input("Enter a number: "))
i = 1

while(i<11):
  print(f"{n} X {i} = { n * i}")