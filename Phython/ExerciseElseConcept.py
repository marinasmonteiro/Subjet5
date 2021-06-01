a= input("Enter a  first number:")
b= input("Enter a seconnd number:")

result= float(a) - float(b)
if result>10:
    print("the result is greater than 10")
elif result>0:
    print("The resulaut is greater than 0 but not than 10")  
elif result==0:
    print("the result is zero")
else:
    print("The result is a negative number")

print("You can try again!")

