# write a program a/b where a and b are integers, if b=o, display infinite by handiling the 'ZeroDivisionError' .


try:
  
  a = int(input("Enter a : "))
  b = int(input("Enter b : "))
  print(a/b)
  
except ZeroDivisionError as v :
  print("Infinite")
  
  
  
# store the multiplication table generated in problem 3 in a file named tables.txt.

n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]

with open("tables.txt", "a") as f:
  f.write(str(table) + "\n")