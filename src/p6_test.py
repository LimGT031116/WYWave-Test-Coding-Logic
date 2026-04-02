from p6 import max_char

input = "Hello, world!"
expected_char = 'l'
expected_occurrence = 3
char, count = max_char(input)
print("Input =", input)
print("Expected Character =", expected_char)
print("Expected Occurrence =", expected_occurrence)
print("Output Character=", char)
print("Output Occurrence=", count)
print("Pass =", (expected_char == char and expected_occurrence == count))