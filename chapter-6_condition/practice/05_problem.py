marks = int(input("Enter your marks: "))

if (marks<=100 and marks>=90):
  grade = "Ex"
elif(marks<90 and marks>=80):
       grade = "A"
elif(marks<90 and marks>=70):
       grade = "B"
elif(marks<90 and marks>=60):
       grade = "C"
elif(marks<90 and marks>=50):
       grade = "D"
elif(marks<90 and marks>=40):
       grade = "E"
       
print("You grade is:", grade)