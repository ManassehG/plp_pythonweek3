def add_numbers(a, b):
    answer = a + b
    return answer

sum = add_numbers(2, 5)
print(f'The sum is {sum}')

def add_numbers2(*nums):
    sum2 = 0
    for num in nums:
        sum2 += num
    return sum2
print(f'The sum is {add_numbers2(2, 3, 4)}')    

def add_ages(**ages):
    sum = 0
    for k, v in ages.items():
        sum += v
    return sum
print(f'Total ages: {add_ages(mutemi =  21, Anita = 22, Moses = 30)}')

#Lamda functions
snack = lambda : print("Juice and Cake")
snack()

num_square = lambda num: num ** 2
print(num_square(3))
        


