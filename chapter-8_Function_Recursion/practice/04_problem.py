# write a py function convert inches to cms.

def inch_to_cms(inch):
  return inch * 2.54

n = int(input("Enter values in inches: "))

print(f"the corresponding value in cms is {inch_to_cms(n)}")