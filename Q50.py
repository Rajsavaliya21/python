# Write a Python function to calculate the factorial of a number (a non-negative integer).
def fac(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    print(sum)


fac(7)
