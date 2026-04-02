# Recursive function to calculate the nth Fibonacci number
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to generate a Fibonacci sequence of a given length
def generate_fibonacci_sequence(count):
    if count < 0:
        raise ValueError("Count must be a non-negative integer")
    sequence = []
    for i in range(count):
        sequence.append(fibonacci_recursive(i))
    return sequence

if __name__ == "__main__":
    # Keep asking until the user enters a valid number between 0 and 100
    while True:
        num = int(input("Enter the number of Fibonacci elements to generate (0-100): "))
        if 0 <= num <= 100:
            break
        print("Invalid input! Please enter a value between 0 and 100.")

    fib_sequence = generate_fibonacci_sequence(num)
    print(fib_sequence)