# Recursion
# When we call a function within other function, that called as recursion.

# def factorial(n):
#     if(n==0 or n ==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# Output
# 6
# 24
# 120

# Fibonacci sequence
def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
nterms = 10
if nterms <= 0:
    print("Please enter a postive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fib(i))