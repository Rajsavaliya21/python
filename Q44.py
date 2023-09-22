# Write a Python program to print all unique values in a dictionary.

d={1:20,2:20,3:40,4:40,5:50}
a=list(i for i in d.values())
se= set(a)
idd=dict()
for s in se : 
    idd[s]=a.count(s)
print(idd)
for i in idd:
    if idd[i]==1:
        print(i)