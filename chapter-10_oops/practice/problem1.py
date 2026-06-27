# create a class "programmer" for storing information of few programmers working at microsoft.

class Programmer:
  company = "Microsoft"
  def __init__(self, name, salary, pin):
   self.name = name
   self.salary = salary
   self.pin = pin
   
   
r = Programmer("Rashi", 1200000, 242006)
print(r.name, r.salary, r.pin, r.company)
y = Programmer("yash", 1200000, 245001)
print(y.name, y.salary, y.pin, r.company)