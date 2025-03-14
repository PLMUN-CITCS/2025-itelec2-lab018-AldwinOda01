def square(num):
    
    return num ** 2

def sum_of_squares(numbers):
   
    total = 0
    for n in numbers:
        total += square(n) 
        
    return total

numbers_list = [2, 3, 4]

result = sum_of_squares(numbers_list)

print(f"The sum of squares is: {result}")
