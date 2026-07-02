def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def is_even(number):
    if number % 2 == 0:
       return "Even"
    return "Odd"

print(square(5))
print(cube(5))
print(is_even(5))

result = (square(3), cube(2), is_even(7))
print(result)
