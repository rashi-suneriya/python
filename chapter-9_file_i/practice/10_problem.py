# write a program to wipe out the content of a file using py.

with open("this_copy.txt", "w") as f:
  f.write("")  # no undestood
  
  
  # write a python program to rename a file to "renamed_by_python.txt"
  
  
with open("old11.txt") as f:
  content = f.read()
  
with open("renamed_by_python.txt", "w") as f:
  f.write(content)  