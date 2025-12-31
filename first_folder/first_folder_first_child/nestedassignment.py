


#task 2 to find the largest and smallest number in the list
numbers = [23, 45, 12, 56, 89, 3, 44]

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest:", smallest)
print("Largest:", largest)
