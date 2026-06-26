# class attribute
class Employee:
  language = "py" # This is a clas attribute
  salary = 1200000
  
  
rashi = Employee()
rashi.language = "js"  #This is an instance(object) attribute
print( rashi.language, rashi.salary)

