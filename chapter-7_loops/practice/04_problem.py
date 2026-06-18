# write a prog find sum of n natural number using while loop.

n = int(input("Enter the number: "))
i = 1
sum = 0
while(i<=n):
  sum += i
  i+=1
  
print(sum)



# find a 5 factorial
# 5! = 1 x 2 x 3 x 4 x5

n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
  product = product * i
  
print(f"The factorial of {n} is {product}")