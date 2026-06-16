# creat an empty dictonary. allow 4 friend to enter their favorite language as value and use key as their name.Assume that the names are unique.

d = {}

name = input("Enter friends neme: ")
lang = input("Enter Language name: ")
d.update({name: lang})
name = input("Enter friends neme: ")
lang = input("Enter Language name: ")
d.update({name: lang})
name = input("Enter friends neme: ")
lang = input("Enter Language name: ")
d.update({name: lang})
name = input("Enter friends neme: ")
lang = input("Enter Language name: ")
d.update({name: lang})
name = input("Enter friends neme: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)