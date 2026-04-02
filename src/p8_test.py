from p8 import anagram_checker

input = [["listen", "silent"], 
         ["debit card", "Bad credit"],
         ["hello", "bye"],
         ["restful", "fluster"],
         ["listen", "silentt"],
         ["Conversation", "Voices, rant on"]]
expected_output = [True,
                   True,
                   False,
                   True,
                   False,
                   True]
output = []

for i in input:
    output.append(anagram_checker(i[0], i[1]))

print("Input =", input)
print("Expected Output =", expected_output)
print("Output=", output)
print("Pass =", expected_output == output)