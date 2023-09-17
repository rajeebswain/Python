
# If a string written after def and before print, then only that is consider as docstring.
# Chaging the docstring chages the program output. 
# if we didn't define the string before print in a function, thtt considers as comment.
# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__)

# Output:
# 25
# Takes in a number n, returns the square of n


def square(n):
    print(n**2)
    '''Takes in a number n, returns the square of n'''
square(5)
print(square.__doc__)