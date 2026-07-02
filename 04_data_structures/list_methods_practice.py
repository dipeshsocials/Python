numbers = [10, 20, 30]
print(numbers)

#append()--- adds one object

numbers.append(40)
print(numbers)

#insert(index, value)

numbers.insert(1, 15)
print(numbers)

#extend() --- adds each object seperately

numbers.extend([50, 60, 70])
print(numbers)

numbers.append([80, 90]) #output (10, 20, 30, 40, 50, 60, 70, [80, 90])
print(numbers)

numbers.extend([80, 90])
print(numbers)

#remove()

numbers.remove(20)
print(numbers)

#pop()

last = numbers.pop()
print(last)
print(numbers)

#specific_index

numbers.pop(2)
print(numbers)

#clear()

numbers.clear()
print(numbers)

#index

fruits = ["Apple", 'Banana', """Mango"""]
print(fruits.index("""Mango"""))

# count

num = [1, 2, 3, 3, 5, 3, 7, 8, 3]
print(num.count(3))

#sort()
#accending

numb = [12, 4, 3, 7, 6, 1, 10]
numb.sort()
print(numb)

#decending

numb.sort(reverse=True)
print(numb)


#reverse()

numbe = [1, 2, 3, 4]
numbe.reverse()
print(numbe)

#copy

a = [1, 2, 3]
b = a.copy()
b.append(4)
b.extend([5, 6])

print(a)
print(b)




