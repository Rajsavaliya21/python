# Write a Python function that checks whether a passed string is a palindrome or not.

def pali(objj):
    return objj==objj[::-1]
k=pali('racecar')
if k == True:
    print(f'the given string is palingdrom')
else:
    print('it is not palingdrom.')
