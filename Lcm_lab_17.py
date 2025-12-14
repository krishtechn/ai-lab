# Program to find LCM of two numbers using GCD

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

g = gcd(a, b)
lcm = (a * b) // g

print("LCM is:", lcm)
