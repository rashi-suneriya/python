# Q8. write a program to make a copy of a text file "this.txt"

with open("this8.txt") as f:
  content = f.read()
  
with open("this_copy.txt", "w") as f:
  f.write(content)  
  
  
  
  #Q9 write a program to find out wheather a file is identical & matches the content of another file.
  
with open("this8.txt") as f:
    content1 = f.read()
    
with open("this_copy.txt") as f:
    content2 = f.read()
    
if(content1 == content2):
    print("Yes these files are identical")
    
else:
    print("No these files are not identical")      