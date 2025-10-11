def sum_divisible_3_not_5():
    total = 0
    for i in range(50, 100):
        if i % 3 == 0 and i % 5 != 0:
            total += i
    return total

x = sum_divisible_3_not_5()
print("Sum of numbers(50-100) which are divisible by 3 and not divisible by 5 are : ",x)