# Write a Python program to create a tuple with different data types.

tuple_data=tuple()
num=int(input("enter the number "))
string=input("entert the char. ")
boll=bool(input("entert the bool value"))
list_for=list()
list_for.append(num)
list_for.append(string)
list_for.append(boll)

tuple_data=list_for
print(tuple_data)
