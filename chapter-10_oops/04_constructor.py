class Employee:
  language = "python" # This is a clas attribute
  salary = 1200000
  
  
  def __init__(self): # dunder method which is automatically called
    print("I am creating an object")
  
  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary} ")
    
  @staticmethod
  def greet():
    print("Good morning")
  
rashi = Employee()
rashi.name = "Rashi"
print(rashi.name, rashi.salary)




# ++++++++++++++++++++++++++++++++++++++++++++


class Employee:
  language = "python" # This is a clas attribute
  salary = 1200000
  
  
  def __init__(self, name, salary, language): 
    print("I am creating an object")
    self.name = name
    self.salary = salary
    self.language = language

  
rashi = Employee("Rashi", 150000, "javascript")
rashi.name = "Rashi"
print(rashi.name, rashi.salary, rashi.language)