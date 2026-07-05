#Method 1 : Basic for loop
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


#Method 2 : using range()
fruits = ["Apple", "Banana", "Mango"]

for i in range(len(fruits)):
    print(i, fruits[i])


#Method 3 : enumerate()
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Using if inside a loop
numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:
   if number % 2 == 0:
     print(number)

# Sum of a list
numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print(total)
# Find the largest number
numbers = [45, 12, 89, 23, 67]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
