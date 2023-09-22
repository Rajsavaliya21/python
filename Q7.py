#  Write a Python program to count the number of strings where the string length is 2 or more, and the first and last character are the same from a given list of strings.
k = input("enter the value j")
if len(k)>=2:
    print("lenth is more than two.")
else:
    print("lenth of string is less than two.")
if k[0]==k[-1]:
    print("the first and last charter is same.")
else:
    print("first and last charter is not same.")