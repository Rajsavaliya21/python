# Write a Python program to remove empty tuple(s) from a list of tuples.



tuple_list = [(1, 2), (), (3, 4), (), (5, 6), ()]

filtered_list = [tup for tup in tuple_list if tup]

print(filtered_list)

