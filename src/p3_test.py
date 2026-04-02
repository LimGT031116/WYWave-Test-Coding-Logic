from p3 import generate_fibonacci_sequence

# Assume fibonacci_recursive(n) and generate_fibonacci_sequence(count) are already defined

# Test case for input = 0
input0 = 0
expected0 = []
output0 = generate_fibonacci_sequence(input0)
pass0 = output0 == expected0
print("Test case 0")
print("Input =", input0)
print("Expected =", expected0)
print("Output =", output0)
print("Pass =", pass0)
print("-" * 30)

# Test case for input = 1
input1 = 1
expected1 = [0]
output1 = generate_fibonacci_sequence(input1)
pass1 = output1 == expected1
print("Test case 1")
print("Input =", input1)
print("Expected =", expected1)
print("Output =", output1)
print("Pass =", pass1)
print("-" * 30)

# Test case for input = 2
input2 = 2
expected2 = [0, 1]
output2 = generate_fibonacci_sequence(input2)
pass2 = output2 == expected2
print("Test case 2")
print("Input =", input2)
print("Expected =", expected2)
print("Output =", output2)
print("Pass =", pass2)
print("-" * 30)

# Test case for input = 5
input5 = 5
expected5 = [0, 1, 1, 2, 3]
output5 = generate_fibonacci_sequence(input5)
pass5 = output5 == expected5
print("Test case 5")
print("Input =", input5)
print("Expected =", expected5)
print("Output =", output5)
print("Pass =", pass5)
print("-" * 30)

# Test case for input = 10
input10 = 10
expected10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
output10 = generate_fibonacci_sequence(input10)
pass10 = output10 == expected10
print("Test case 10")
print("Input =", input10)
print("Expected =", expected10)
print("Output =", output10)
print("Pass =", pass10)
print("-" * 30)