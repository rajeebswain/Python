# Docstring
##### If a string written after def and before print, that consider as docstring.
##### Chaging the docstring chages the program output. 
##### if we didn't define the string before print in a function, thtt considers as comment.
### Case-1
```
def square(n):
     '''Takes in a number n, returns the square of n'''
     print(n**2)
square(5)
print(square.__doc__)
```
#### Output:
```
25
Takes in a number n, returns the square of n
```
### Case-2
```
def square(n):
     print(n**2)
     '''Takes in a number n, returns the square of n'''
square(5)
print(square.__doc__)
```
##### Here the string defined after the print, so the doc-string printed "none".
##### And the string considered as comment.

#### Output:
```
25
None
```