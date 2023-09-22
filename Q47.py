# Write a Python program to find the highest 3 values in a dictionary.
d = {
    1: 20,
    2: 50,
    3: 100,
    4: 60,
    5: 111,
}
max1 = d[1]
max2 = d[1]
max3 = d[1]

for i in d.values():
    if max1 < i:
        max1 = i
# print(max)
for i in d.values():
    if max2 < i and i != max1:
        max2 = i
for i in d.values():
    if max3 < i and i != max1 and i != max2:
        max3 = i
print(max1)
print(max2)
print(max3)
