numbers = input("Enter the list (separated by commas): ").split(",")

duplicates = []
counts = []

for element in numbers:
  if numbers.count(element) > 1 and element not in duplicates:
    duplicates.append(element)
    counts.append(numbers.count(element))
  else:
    print("No duplicate elements.")

for i in range(len(duplicates)):
  print(f"Element {duplicates[i]} repeats {counts[i]} times.")