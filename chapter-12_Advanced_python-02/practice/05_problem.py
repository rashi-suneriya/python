# write a program to find the maximum of the numbers in a list using the reduce function.


from functools import reduce 
l = [111, 2,65, 54, 667, 34, 23, 90, 12, 45]

def greater(a, b):
  if (a>b):
    return a
  return b

print(reduce(greater, l))