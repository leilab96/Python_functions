#First excercise
#A function that finds all numbers between two arbitrary values (e.g. between 2000 and 3200) that can be divided by 7 but not by 5.

def divisible_numbers(start, end, divided, non_divided):
    numbers = []
    for num in range(start, end+1):
        if num % divided == 0 and num % non_divided != 0:
            numbers.append(num)
    return numbers

print(divisible_numbers(0,35,7,5))
print(divisible_numbers(2000,3200,7,5))
