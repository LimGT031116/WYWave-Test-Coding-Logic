from p9 import node_path_existence

input = [['D', 'B'], 
         ['F', 'A'],
         ['G', 'C'],
         ['E', 'D']]

expected_output = [[True, ['D', 'E', 'F', 'B']],
                   [True, ['F', 'B', 'A']],
                   [False, []],
                   [True, ['E', 'F', 'B', 'D']],]

output = []

for i in input:
    output.append(node_path_existence(i[0], i[1]))

print("Input =", input)
print("Expected Output =", expected_output)
print("Output=", output)
print("Pass =", expected_output == output)