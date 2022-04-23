# Checking if a number is prime or not

def isprime(num):
    if num > 1:
        for n in range(2,num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False
print(isprime(13))
print(isprime(24))