# Write a Python program to check whether a list contains a sub-list.


def contains_sublist(main_list, sub_list):
    for i in range(len(main_list) - len(sub_list) + 1):
        if main_list[i:i+len(sub_list)] == sub_list:
            return True
    return False

main_list = [1, 2, 3, 4, 5, 6, 7]
sub_list = [3, 4, 5]
result = contains_sublist(main_list, sub_list)

if result:
    print("The main list contains the sub-list.")
else:
    print("The main list does not contain the sub-list.")
