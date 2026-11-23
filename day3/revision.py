name = input("Enter your name: ")
marks = int(input("Enter your marks out of 100: "))

print(name)
print(marks)

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Fail")