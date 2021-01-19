def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divisible(num1,num2):
    return num1/num2
    
num1 = int(input("ener tbe 1st num:"))
operation = input("enter yiur operation(+,-,*,/)")
num2 = int(input("enter yhe 2nd num"))

result =0
if operation == "+":
    result = add(num1,num2)
elif operation == "-":
    result = subtract(num1,num2)
elif operation == "*":
    result = multiply(num1,num2)
elif operation == "/":
    result = divisible(num1,num2)
else:
    print("pls enter your operation")
    
print(num1,operation,num2,"=",result)
    