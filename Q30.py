# Write a Python program to unzip a list of tuples into individual lists.

tu_1=[(91,2),(1212,121212),21221]
for i in range(len(tu_1)):
    print(tu_1[i])
    if type(tu_1[i])==tuple:
        l_1=list(tu_1[i])
        tu_1[i]=l_1

print(tu_1)
print("hello")

