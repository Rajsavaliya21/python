# Write a Python function to check whether a number is in a given range.

def chec(num,rang):
    isit=False
    for i in range(rang):
        if num == i:
            isit=True
            break
    if isit==True:
        print("it is in the range.")
    else:
        print('it is not in the range.')
chec(10,9)
