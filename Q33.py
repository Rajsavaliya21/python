# Write a Python script to sort (ascending and descending) a dictionary by value.
d_1={1:2,2:1,3:3}
l_1=list()
for i in d_1.values():
    l_1.append(i)
l_1.sort()
for i,o in zip(d_1,l_1):
    # print(l_1)
    d_1[i]=o
print("after change",d_1)
