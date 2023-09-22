# Write a Python function to check whether a number is perfect or not.

def is_perfect_number(n):
    if n <= 0:
        return False
    divisors = [1]  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  
                divisors.append(n // i)
    return sum(divisors) == n
num = 28  
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")