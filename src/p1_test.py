from p1 import sort_numbers

# Test input
input_list = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]
expected_output = [-36, -16, -3, 8, 21, 28, 55, 77, 99, 111, 400]

# Run the function
result = sort_numbers(input_list.copy())

# Print results
print("Input: ", input_list)
print("Sorted output: ", result)
print("Expected output: ", expected_output)
print("Test passed: ", result == expected_output)