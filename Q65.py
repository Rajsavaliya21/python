# 65. Write a Python program to return the sum of all divisors of a number.

def sum_of_divisors(n):
    divisor_sum = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_sum += i
    
    return divisor_sum

number = int(input("Enter a number: "))

result = sum_of_divisors(number)
print(f"The sum of divisors of {number} is {result}")



