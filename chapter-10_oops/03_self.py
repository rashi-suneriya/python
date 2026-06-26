class Employee:
  language = "python" # This is a clas attribute
  salary = 1200000
  
  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary} ")
    
    # static methode
  @staticmethod
  def greet():
    print("Good morning")
  
rashi = Employee()
print( rashi.language, rashi.salary)
rashi.greet()
rashi.getInfo()