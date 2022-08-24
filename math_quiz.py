#for this one i watched a tutorial and then the next day i tried making it from memory,of course i changed the topic and questions

print("Welcome to my math game!")
score = 0
#Question 1
answer = input("What is 2+2? ")
answer = str(answer)

if answer.isdigit():
    if answer == "4":
     score += 1
     print("Correct")
    else:
     print("Incorrect")
else:
    print("Please input a number next time")


#Question 2
answer = input("What is 3x9? ")
answer = str(answer)

if answer.isdigit():
    if answer == "27":
     score += 1
     print("Correct")
    else:
     print("Incorrect")
else:
    print("Please input a number next time")


#Question 3
answer = input("What is 48:4? ")
answer = str(answer)

if answer.isdigit():
    if answer == "12":
     score += 1
     print("Correct")
    else:
     print("Incorrect")
else:
    print("Please input a number next time")


#Question 4
answer = input("What is 2x(3x3) ")
answer = str(answer)

if answer.isdigit():
    if answer == "18":
     score += 1
     print("Correct")
    else:
     print("Incorrect")
else:
    print("Please input a number next time")


#Question 5
answer = input("What is 10x10x10x10? ")
answer = str(answer)

if answer.isdigit():
    if answer == "10000" :
     score += 1
     print("Correct")
    else:
     print("Incorrect")
else:
    print("Please input a number next time") 

print("You got " + str(score) + " questions right out of 5!")     