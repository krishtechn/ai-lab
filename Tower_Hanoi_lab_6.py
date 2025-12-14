# Program to solve Tower of Hanoi using recursion

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
    else:
        hanoi(n - 1, source, destination, auxiliary)
        print("Move disk", n, "from", source, "to", destination)
        hanoi(n - 1, auxiliary, source, destination)

# Input number of disks
n = int(input("Enter number of disks: "))

print("\nSteps to solve Tower of Hanoi:")
hanoi(n, 'A', 'B', 'C')
