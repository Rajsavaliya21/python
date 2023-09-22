# 22. Write a Python program to convert a tuple to a string.

tuple_1=('sarvesh','raj','vasu')
list_1=list(tuple_1)

string=str()
for i in list_1:
    string+=i

print(string)
