# Program to find the Fibonacci number at a given position

n = int(input("Enter the position: "))

a, b = 0, 1

if n == 0:
    print("Fibonacci number:", a)
elif n == 1:
    print("Fibonacci number:", b)
else:
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    print("Fibonacci number:", b)
