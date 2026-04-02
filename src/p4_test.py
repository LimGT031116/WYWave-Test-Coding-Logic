from p4 import list_intersection

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]
expected = [4, 5, 6]
output = sorted(list_intersection(list1, list2))
print("Input list1 =", list1)
print("Input list2 =", list2)
print("Expected =", expected)
print("Output =", output)
print("Pass =", output == expected)