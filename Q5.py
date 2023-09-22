# 5. Write a Python function to get the largest number, smallest number, and sum of all from a list.

list_a=[1,2,3,5,2,8,2,1]
max=list_a[0]
min=list_a[0]
sum=list_a[0]
for i in list_a:
    if max<i:
        max=i
    if min>i:
        min=i
    if sum != i:
        sum+=i
print(max)
print(min)
print(sum)