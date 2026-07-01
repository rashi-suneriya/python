# create a class 'pets' from a class 'Animals' and further created a class 'Dog' from 'pet'. Add a method 'bark' to class'Dog'.

class Animals:
  pass

class Pets(Animals):
  pass

class Dog(Pets):
  
  @staticmethod
  def bark():
    print("Bow Bow!")
    
d = Dog()
d.bark()  