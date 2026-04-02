from p5 import symmetric_difference

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]
expected = [1, 2, 3, 7, 8, 9]
output = sorted(symmetric_difference(list1, list2))
print("Input list1 =", list1)
print("Input list2 =", list2)
print("Expected =", expected)
print("Output =", output)
print("Pass =", output == expected)