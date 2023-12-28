print("Welcome to the Maths bowl")
name = input("Enter your name>> ")
print("Hi", name)
age = int(input("Enter your age >> "))


if age < 14 and age > 2:
    print("You are eligible for the contest....")
    option = input("Proceed to the next stage, YES or NO? ")
    if option.lower() == "yes":
        print("Let's proceed......")
        quest = int(input("if x + 2 = 10 then x = "))
        if quest == 8:
            print("You're correct!")
        else:
            print("You're wrong!")
    elif option.lower() == "no":
        print("You have opted out of the competition")
    else:
        print("I don't understand you")
elif age <= 2:
    print("You are too young to participate")
elif age >= 14:
    print("You are too old to participate")
else:
    print("Not Valid!")