# create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o.a does this change the class attribute?

# ans is = No

class Demo:
  a = 4
  
o = Demo()
print(o.a) # print the class attribute because instance attribute is not present
  
o.a = 0 # instance attribute is set
print(o.a) #prints the instance attribute because instance attribute is present

#print(Demo.a) # prints the class attribute