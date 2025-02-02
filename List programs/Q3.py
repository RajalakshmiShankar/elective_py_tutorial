master_list = [10, 25, 7, 18, 30, 5, 12]
print("The List:",master_list)
limit= int(input("Enter a limit number: "))
filtered_list = [num for num in master_list if num < limit]

print("Numbers less than", limit, ":", filtered_list)
