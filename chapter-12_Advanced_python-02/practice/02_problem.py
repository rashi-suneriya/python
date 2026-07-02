# write a program to input name, marks and phone numbers of a student and format it using the format function like below:
# "The name of the student is Rashi, her marks are 90 and her phone number is 1234567890"


name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = input("Enter phone number: ")

s = "The name of the student is {}, her marks are {} and her phone number is {}".format(name, marks, phone)
print(s)