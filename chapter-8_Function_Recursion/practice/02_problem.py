#  write a py prog using function to convert celsius to fahrenheit

def f_to_c(f):
  return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)} c")



#  how to prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c", end="")
print("d", end="")


# write a recursive function to calculate the sum of first n natural numbers.


'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3

sum(n) = 1 + 2 + 3 + 4...... n-1 + n
sum(n) = sum(n-1) + n
'''

def sum(n):
  if(n==1):
    return 1
  return sum(n-1) + n

print(sum(4))