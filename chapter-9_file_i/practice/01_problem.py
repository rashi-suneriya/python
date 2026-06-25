#  write a program to read the text from a given file 'poems.txt' anf find out wheather it contains the word 'twinkle'.


f = open("poem.txt")
content = f.read()
if("twinkle" in content):
  print("The word twinkle is present in the content")
  
else:
  print("The word twinkle is not present in the content")
  
f.close()    