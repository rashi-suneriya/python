# we are going to write a program that generates a random number and the user to guess it.

# if the player's guess in higher then the actual no. , the peogram displays "Lower number please". similarly, if the user's guess is too low, the program prints "higher number please". when the user guesses the correct number, the program displays the no. of guesses the player used to arrive at the number.



import random
n = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a > n):
      print("Lower number please")
      guesses +=1
    elif(a<n):
      print("Higher number please")
      guesses +=1
      
      
print(f"you have guesses the number {n} correctly in {guesses} atempts")