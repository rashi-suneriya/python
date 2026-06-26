# a file contains a words "Donkey" multiple times. you need to write a program which replace this word ##### by updating the same files.

word = "donkey"

with open("file4.txt", "r") as f:
  content = f.read()
  
contentNew = content.replace(word, "######")

with open("file4.txt" , "w") as f:
  f.write(contentNew)  
  
  
  
# Q5 reapeat program 4 for a list of such words to be same file.
  
  
words = ["donkey", "bad", "good"]

with open("file4.txt", "r") as f:
  content = f.read()
  
for word in words:  
 content = content.replace(word, "#" * len(word))

with open("file4.txt" , "w") as f:
  f.write(content)  
  
  
  
# Q6 write a program to mine a log file and find out wheather it contains 'python'.
  
# with open("log6.txt") as f:
#     content = f.read()
    
# if("python" in content):
#   print("Yes py is present")
# else:
#   print("No py is not present")      
  
  
  # Q7 add line no. in Q6
  
  with open("log6.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:    
 if("python" in line):
  print(f"Yes python is present. Line no: {lineno}")
  break
 lineno += 1
else:
  print("No python is not present")      