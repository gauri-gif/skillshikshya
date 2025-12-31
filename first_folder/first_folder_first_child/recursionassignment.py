

#task1
def palindrome(s):
    if len(s)<=1:
        return True
    else:
        if s[0]!=s[-1]:
            return False
        return palindrome(s[1:-1])       
        
s=input("Enter the string( level):")
if palindrome:
    print("palindrome ")
else:
    print("not palindrome")

(palindrome(s))      




#task 2
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter any number : "))
print(sum_of_digits(number))

