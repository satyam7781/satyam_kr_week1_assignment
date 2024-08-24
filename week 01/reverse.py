'''Write a script that accepts user input and
displays it in reverse order.'''

#defining a Function to reverse a script
def reverse_input():
    #accepting user input
    user_input = input("Please enter a string: ")
    #reversing the input
    reversed_input = user_input[::-1]
    #displaying the reversed input
    print("Reversed input: ", reversed_input)

reverse_input()