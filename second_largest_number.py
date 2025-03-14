

numbers = input("Enter a list of numbers (separated by commas): ").split(",")
numbers = [int(number) for number in numbers]

largest = max(numbers)
numbers.remove(largest)

second_largest = max(numbers)

print("The second largest number is:", second_largest)