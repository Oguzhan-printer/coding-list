numbers_list = input("Enter a list of numbers (separated by commas): ").split(",")
numbers_list = [int(num) for num in numbers_list]

new_numbers_list = []

for num in numbers_list:
    if num > 0 :
        multiply = num*2 
        new_numbers_list.append(multiply)
    elif num < 0 :
        multiply = num*2
        new_numbers_list.append(multiply)
    else:
        new_numbers_list.append(num)

print(new_numbers_list)
             


       


    



        