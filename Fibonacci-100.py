# Define the function to calculate the nth Fibonacci number
def fib(n):
    if n <= 0:
        print("Input should be positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Generate and print the first 100 Fibonacci numbers
for i in range(1, 101):
    print(f"Fibonacci({i}) = {fib(i)}")