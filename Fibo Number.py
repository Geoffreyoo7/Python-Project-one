import math
# if the number is perfect square, else this will return false
def isPerfectSquare(num):
    s =int(math.sqrt(num))
    return s*s == num

def isFibonacciNumber(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

n = int(input("Enter a number"))
if(isFibonacciNumber(n) == True):
    print(n, "is a Fibonacci number")
else:
    print(n, "is not a fibonacci number")