class Employee:
  company = "ITC"
  def show(self):
    print(f"The name of the employe is {self.name} and the salary is{self.salary}")
    
class Programmer(Employee):
  company = "ITC Infotech"
  def showLanguage(self):
    print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

# a.show("rashi", "40000")
print(a.company, b.company)