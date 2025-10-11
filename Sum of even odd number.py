def sum_of_even_odd_num(numbers):
    odd_sum=0
    even_sum=0

    for x in numbers:
        if x%2==0 :
            even_sum += x
        else:
            odd_sum += x
    return even_sum,odd_sum


numbers=[2,7,54,3,9,12,19,4]
a,b=sum_of_even_odd_num(numbers)
print("Sum of Even numbers : ",a)
print("Sum of Odd numbers : ",b)


