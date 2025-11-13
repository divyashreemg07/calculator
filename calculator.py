def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "Error: The Denominator cannot be zero"
    else:
        return a/b

def calculator():
    while True:
        print("\nSelect operation: \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")  
        
        option=input("Enter your option (1/2/3/4/5):")

        if option not in ('1','2','3','4','5'):
            print("Invalid option! Please provide a valid option")
            continue

        if option=='5':
            print("Exit")
            break

        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
        except ValueError:
            print("Invalid Input! please provide numeric values")
            continue

        if option=='1':
            result=add(num1,num2)
            print(f"The sum of  {num1}+{num2} is {result}")

        elif option=='2':
            result=subtract(num1,num2)
            print(f"The difference of  {num1}-{num2} is {result}")

        elif option=='3':
            result=multiplication(num1,num2)
            print(f"The product of  {num1}*{num2} is {result}")

        elif option=='4':
            result=division(num1,num2)
            print(f"The division of  {num1}/{num2} is {result}")

calculator()


