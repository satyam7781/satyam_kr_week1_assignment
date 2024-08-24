'''
2Create a program that uses conditional
statements to determine if a number is positive,
negative, or zero.'''
# Define a function to check the sign of a number
def check_sign(num):
    # Use if-elif-else statements to determine the sign of the number
    if num > 0:
        return "Positive"
    elif num <0:
        return "Negative"
    else:
        return "Zero"
    
num=int(input("Enter a number "))
   
print(check_sign(num))

    