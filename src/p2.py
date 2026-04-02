def fizz_buzz(array):
    result = []  # List to store results
    for i in array:
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")  # Divisible by 3 and 5
        elif i % 3 == 0:
            result.append("Fizz")      # Divisible by 3
        elif i % 5 == 0:
            result.append("Buzz")      # Divisible by 5
        else:
            result.append(i)           # Not divisible by 3 or 5
    return result