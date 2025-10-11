def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

a=input("Write a number to find factorial: ")
fact= factorial(a)
print("Factorial is : ",fact)