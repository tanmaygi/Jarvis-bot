# jarvis bot start
print("Hello! My name is Jarvis.")
print("I was created in 2021.")
print("Please, remind me your name.")
your_name = input()
# String Concatenation
print("What a great name you have, " + your_name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

# Get the input from user
rem3 = int(input("Remainder by 3:"))
rem5 = int(input("Remainder by 5:"))
rem7 = int(input("Remainder by 7:"))

# Based on simple math trick
# It turns out that for each number ranging from 0 to 104 the calculation will result in the number itself. 
# This perfectly fits the ordinary age range, doesn't it!
user_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print("Your age is " + str(user_age) + "; that's a good time to start programming!")

# counter – a variable that changes its value after each iteration.
print("Now I will prove to you that I can count to any number you want.")
num = int(input())
counter = 0
while counter <= num:
    print(str(counter) + " !")
    counter += 1 
print("Completed, have a nice day") 

 # MCQ test
print("Let's test your programming knowledge.")

print("Why do we use methods?")
optiona = print("To repeat a statement multiple times.")
optionb = print("To decompose a program into several small subroutines.")
optionc = print("To determine the execution time of a program.")
optiond = print("To interrupt the execution of a program.")
  
option = [optiona, optionb, optionc, optiond]
# ans = int(input())
# if ans == 2:
#     print()