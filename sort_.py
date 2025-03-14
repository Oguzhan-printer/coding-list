
numbers = input("Enter the list (separated by commas): ").split(",")

ascending_order = sorted(numbers, key=int)
descending_order = sorted(numbers, key=int, reverse=True)

print("Ascending order: ", ascending_order)
print("Descending order: ", descending_order)


