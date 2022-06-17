# File Name: interpreter.py
# Author Name: Lindsey Kim
# Date: 11/4/2020
# Course: COSC 1
# Short Description: This gives the answer to a Reverse Polish Expression
#

def compute_rpn(string):
    rpn = string.split()  # splits the string into an array
    stack = []  # creates the stack array

    for i in range(len(rpn)):
        if rpn[i] == "/":  # checks if the next token is a division operator
            number_one = stack.pop()  # takes the first number from the stack
            number_two = stack.pop()  # takes the second number from the stack
            op = number_two//number_one  # divides the two numbers
            stack.append(op)  # adds the quotient to the stack

        elif rpn[i] == "+":  # checks if the next token is an addition operator
            number_one = stack.pop()  # takes the first number from the stack
            number_two = stack.pop()  # takes the second number from the stack
            op = number_two + number_one  # adds the two numbers
            stack.append(op)  # adds the sum to the stack

        elif rpn[i] == "-":  # checks if the next token is a subtraction operator
            number_one = stack.pop()  # takes the first number from the stack
            number_two = stack.pop()  # takes the second number from the stack
            op = number_two - number_one  # subtracts the two numbers
            stack.append(op)  # adds the difference to the stack

        elif rpn[i] == "*":  # checks if the next token is a multiplication operator
            number_one = stack.pop()  # takes the first number from the stack
            number_two = stack.pop()  # takes the second number from the stack
            op = number_two * number_one  # multiplies the two numbers
            stack.append(op)  # adds the product to the stack

        else:
            stack.append(int(rpn[i]))  # if the token is a number, adds it to the stack

    return stack[0]  # returns the result


print(compute_rpn("5 4 -"))  # should print 1
print(compute_rpn("10 3 *"))  # should print 30
print(compute_rpn("10 6 + 3 -"))  # should print 13
print(compute_rpn("84 6 9 + 3 * 3 - /"))  # should print 2
print(compute_rpn("12 5 2 - + 3 6 * -"))  # should print -3
print(compute_rpn("5 13 1 - 4 / + 4 *"))  # should print 32
print(compute_rpn("10 11 6 1 - + 4 / + 4 *"))  # should print 56
