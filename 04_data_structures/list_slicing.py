numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[1:4])  # output (20, 30, 40) 
                    # it does not include the last position
print(numbers[ :4]) 
print(numbers[3: ])
print(numbers[ : ])

# list[start : stop : step]

print(numbers[ : : 2]) #take every second element

print(numbers[ : : -1]) #revese the list

print(numbers[-1]) #neg indexing

print(numbers[-4: ])

print(numbers[-6:-2])

