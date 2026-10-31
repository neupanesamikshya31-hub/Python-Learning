
fullname = input("Enter your full name: ")
id = int(input("Enter your voter ID: "))
age = int(input("Enter your age: "))
province = input("Which province are you from: ")

print("=========================")
title = "registration information"
print(title.upper())
print("=========================")

fullname = fullname.strip()

print("Full Name:", fullname)
print("Voter ID:", id)
print("Age:", age)
print("Province:", province)

answer = input("Do you want to continue? ")

if answer.strip().lower() == "yes":
    print(" ")
    print("Continuing.......")

    if age < 18:
        print("You are not eligible to vote")
    else:
        print("You meet the age requirement.")

else:
    print("Program stopped.")
