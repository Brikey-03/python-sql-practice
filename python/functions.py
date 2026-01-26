# Function to calculate factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # factorial(n) = n * factorial(n-1), stops when n == 0

# Function to calculate sum of first n natural numbers
def sum_n(n):
    return n * (n + 1) // 2

print("Factorial of 5:", factorial(5))
print("Sum of first 10 numbers:", sum_n(10))
