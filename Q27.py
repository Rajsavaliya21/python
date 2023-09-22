# Write a Python program to replace the last value of tuples in a list.

t_1=(1,2,3,4,5,6,7)
t_1=list(t_1)
t_1[-1]=10
t_1=tuple(t_1)
print(t_1,type(t_1))