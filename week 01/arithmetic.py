# Write a Python program to perform basic arithmetic operations (addition, subtraction,multiplication, division).



def arithmetic(Num1,Num2,Choice):
# Addition
    if Choice==1:
        print("Addition of two numbers is ", Num1 + Num2)

#Substraction
    elif Choice==2:
        print("Substraction of two numbers is ", Num1 - Num2)

#Multiplication    
    elif Choice==3:
        print("Multiplication of two numbers is ", Num1 * Num2)

#Division
    elif Choice==4:
        print("Divison of two numbers is ", Num1 / Num2) 

    else:
        print("Invalid Choice")

Num1=int(input("Enter first number "))
Num2=int(input("Enter second number "))
Choice=int(input("Enter your operations \n"
                 "1. Addition \n"
                "2. Substraction \n"  
                "3. Multiplication \n" 
                "4. Divison \n"))
arithmetic(Num1,Num2,Choice)