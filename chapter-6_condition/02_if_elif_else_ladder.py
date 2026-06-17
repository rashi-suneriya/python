# if elif else ladder
a = int (input("Enter your age:"))

if(a>=18):
  print("you are above the age of consent")
  print("Good for you")
  
elif(a<0):
  print("you are entering an invalid -ve age of consent")
  
elif(a==0):
  print("you are entering 0 which is not a valid age of consent")
  
  
else:
  print("you are below  the age of consent")
  print("bad for you")
  
  print("End of program")