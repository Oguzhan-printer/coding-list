from random import shuffle

list_to_shuffle = input("Enter a list of numbers (separated by commas): ").split(",")

shuffle(list_to_shuffle)  # Shuffle the list in place

print(list_to_shuffle)  # Prints the shuffled list