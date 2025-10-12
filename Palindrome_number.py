def palindrome(num):
    rev_num=0
    org_num=num
    while num !=0 :
        rem=num%10
        rev_num= rev_num * 10 + rem
        num=num//10
    return rev_num

num =int(input("Write a number to check palindrome : "))

x=palindrome(num)
print(x)
if x == num :
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number")