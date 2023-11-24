my_list = [1, 2, 3, 4, 5]

index_to_check = 5  # Index to check if it's out of range

if index_to_check >= len(my_list) or index_to_check < -len(my_list):
    print("Index is out of range")
else:
    print("Index is within the range of the list")
