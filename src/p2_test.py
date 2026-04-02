from p2 import fizz_buzz

# Test fizz_buzz for numbers 1 to 15
input_data = list(range(1, 16))
expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
            11, "Fizz", 13, 14, "FizzBuzz"]

output = fizz_buzz(input_data)  # Run function

print("Output:", output)         # Show result
print("Expected:", expected)     # Show expected
print("Pass?", output == expected)  # Check if 

