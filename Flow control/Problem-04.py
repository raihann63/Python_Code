name=str(input("Type first name = "))
dept=str(input("Enter the dept. name = "))
name2=str(input("Type second name = "))
dept2=str(input("Enter the dept. name = "))

print("\n"+"."*50 +"\n")

if name=='Raihan':
    print("Welcome Mr.")
    if dept=='CSE':
         print("You are correct Mr.RAIHAN")
    else:
         print("Please Try again")
elif name2=="Rafi":
     print("Welcome guyes")
     if dept2=="CSE":
         print("You are correct Mr.Rafi ")
     else:
         print("Please try again")            
else:
    print("Both were wrong")
