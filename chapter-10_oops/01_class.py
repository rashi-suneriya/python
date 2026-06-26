class Employee:
  language = "py" # This is a clas attribute
  salary = 1200000
  
  
rashi = Employee()
rashi.name = "Rashi"  #This is an instance(object) attribute
print(rashi.name, rashi.language, rashi.salary)

yash = Employee()
yash.name = "yash yes yashhh..."
print(yash.name, yash.salary, yash.language)

# Here name is instance attribute and salary and language attribute as they directly belong to the class