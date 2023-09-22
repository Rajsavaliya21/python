# Write a Python program to find the repeated items of a tuple.

t_1=(1,1,2,2,3,3,4,5,6,6,8,7,8)
dict_repeat=list()
set_t=set(t_1)

for i in set_t:
    if t_1.count(i)>1:
        dict_repeat.append(i)
print(dict_repeat)   


