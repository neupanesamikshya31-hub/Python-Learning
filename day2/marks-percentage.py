print("=====================================")
print("Hey there! Calculate your total marks and percentage")
print("=====================================")

math=int(input("Enter your math marks: "))
computer=int(input("Enter your computer marks: "))
english=int(input("Enter your english marks: "))

total=math+computer+english
average=total/3
percentage=(total/300)*100
print("Total marks:", total)
print(f"Average marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")