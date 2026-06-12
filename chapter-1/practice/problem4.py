# write a py program toprint content of a directory usin the os module. search online for the function which does that.



import os

directory_path = '/'  

contents = os.listdir(directory_path)

for item in contents:
  print(item)
                     