from p7 import integer_sqrt

input = [4, 9, 16, 25, 36]
expected_output = [2, 3, 4, 5, 6]
output = []

for x in input:
    output.append(integer_sqrt(x))

print("Input =", input)
print("Expected Output =", expected_output)
print("Output=", output)
print("Pass =", expected_output == output)