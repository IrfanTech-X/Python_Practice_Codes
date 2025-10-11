def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


numbers = (1, 2, 3, 4, 5)
result = sum_numbers(numbers)
print("Sum of passing is: " , result)