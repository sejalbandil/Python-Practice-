#This code asks the user to enter their name and their age. Then it prints out a message that tells them the year that they will turn 100 years old!
name = raw_input ("Enter your name: ")

age = input ("Enter your age: ")
y = (100 - age)+2020
print(name+ ", you will turn 100 in " + str(y))
