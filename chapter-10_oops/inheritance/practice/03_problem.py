#  create a clas 'Employee' and add salary and increament properties to it.
# write a method 'salaryAfterIncreament' method with a @property decorator with a setter which changes the values of increment based on the salary.

class Employee:
  salary = 234
  increment = 20
  
  @property
  def slaryAfterIncrement(self):
    return(self.salary + self.salary * (self.increment/100))
  
  @slaryAfterIncrement.setter
  def salaryAfterIncrement(self, salary):
    self.increment = ((salary/self.salary) -1)*100
    
e = Employee()
# print(e.salaryAfterIncrement)
e.slaryAfterIncrement = 280.8
print(e.increment)
