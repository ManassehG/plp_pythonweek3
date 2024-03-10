#Question 1
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

num1 = large_power(20, 20)
num2 = large_power(30, 1)
print(num1)
print(num2)
#Question 2
def divisible_by_ten(num):
    
    rem = num % 10
    
    if rem == 0:
        return True
    else:
        return False

number = divisible_by_ten(20)
number2 = divisible_by_ten(22)
print(number)
print(number2)
    