# write a prog to print star pattern
#   *
#  ***
# *****   for n =3



n = int(input("Enter a number: "))
for i in range(1, n+1):
  print(" "* (n-i), end="")
  print("*"* (2*i-1), end="")
  print(" ")
  
  
# write a prog to print star pattern
#  *
#  ***
#  ****   for n =3  

n = int(input("Enter a number: "))
for i in range(1, n+1):
  print("*"* i, end="")
  print(" ")
  
  
  # write a prog to print star pattern
#  ****
#  *  *
#  ****   for n =3  


n = int(input("Enter a number: "))
for i in range(1, n+1):
  if(i==1 or i==n):
    print("*"* n, end="")
  else:
    print("*", end="")  
    print(" "* (n-2), end="")
    print("*", end="")
  print("")  
  
  
  # problem 10
  
n = int(input("Enter a number: "))

for i in range(1, 11):
  print(f"{n} X {11 - i} = {n*(11-i)}")