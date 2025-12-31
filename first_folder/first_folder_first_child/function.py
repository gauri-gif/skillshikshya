# num=[2,3,4,4,5]
# print(len(num))
# print(type(num))

# for i in range(5):
#     print("My name is gauri")



# num1=int(input("Enter the first number :"))
# num2=int(input("Enter the second number "))
# num3= int(input("Enter the third number"))
# def greatest_num(num1, num2, num3):
#     print(type(num1))
#     print(type(num2))
#     print(type(num3))
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3

# result = greatest_num(num1, num2, num3)

# print(f"The greatest number among {num1}, {num2} and {num3} is {result}")


# def greatest_num(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3

# result = greatest_num(num1, num2, num3)

# print(f"The greatest number among {num1}, {num2} and {num3} is {result}")



# def greet_name(name,grade):
#     return f" My name is {name} i read in class{grade}"


# print(greet_name("Gauri",10))


# def greet_name(name=None,grade=None):
#     return f" My name is {name} i read in class{grade}"

# print(greet_name(grade=10, name="gauri"))


# def volume_cuboid(length,breadth,height):
#     return length*breadth*height
# print(volume_cuboid(45,33,66))



# def reverse_list(lst):
#     reversed_list = []
#     for i in range(len(lst) - 1, -1, -1):
#         reversed_list.append(lst[i])
#     return reversed_list

# my_list = [1, 2, 3, 4, 5]

# result = reverse_list(my_list)
# print("Original list:", my_list)
# print("Reversed list:", result)




# def reverse_list(lst):
#     rev = []
#     for i in lst:
#         rev.insert(0, i)
#     return rev

# my_list = [1, 2, 3, 4]
# print(reverse_list(my_list))



# def reverse_list(lst):
#     return lst[::-1]

# my_list = [134, 2565,653, 564]
# print(reverse_list(my_list))




# def reverse(marks):
#     for i in range (len(marks)):
#         marks[i]=

# 

# def message(num):   
#     for i in range(num):
#         print("hello my name is gauri")

# n = int(input("Enter how many times you want to print: "))
# message(n)



#recursive function


# def message(n):
#     if n==0:
#         return
#     print("Hello my name is Gauri")
#     message(n-1)

# (message(3))


# def fibonacci (n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return(fibonacci(n-1))+ fibonacci(n-2)
    
# print(fibonacci(6))  



# def fibonacci (n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return(fibonacci(n-1))+ fibonacci(n-2)
    
# print(fibonacci(6))  
# 
# 
# 

# def fibonacci (n):
#     if n<=1:
#         return n
#     else:
#         return(fibonacci(n-1))+ fibonacci(n-2)
    
# print(fibonacci(5))  




# def sum_natural(n):
#     if n == 1:       
#         return 1
#     return n + sum_natural(n-1)

# n = int(input("Enter a number: "))
# print("Sum of first", n, "natural numbers is", sum_natural(n))




# n= int(input("Enter the number:"))

# def sum_natural(n):
#     if n==1:
#         return n
    
#       return n + sum_natural(n-1)
# print(f"sum of natural number is {sum_natural(n)} ")





# n= int(input("Enter the number:"))

# def sum_natural(n):
#     if n==1:
#         return n
#     else:
#       return n + sum_natural(n-1)
# print(f"sum of natural number is {sum_natural(n)} ")





# def is_palindrome(s):
#     if len(s) <= 1:  # base case
#         return True
#     if s[0] != s[-1]:  # first and last char not same
#         return False
#     return is_palindrome(s[1:-1])  # check middle part

# word = input("Enter a word: ")
# if is_palindrome(word):
#     print("Palindrome")
# else:
#     print("Not a palindrome")



#from the list find the smallest number using the recursive function 

# input_list=[0,1,2,3,4,5]

# def smallest_number(input_list):
#     if len(input_list)==1:
#         return  input_list[0]
#     else:
#         #



# input_list=[0,1,2,3,4,5]

# def smallest_number(input_list):
#     if len(input_list)==1:
#         return  input_list[0]
#     else:
#         smallest_number= largest   


# numbers = [5, 2, 9, 1, 7]
# def smallest(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#      return min(lst[0], smallest(lst[1:]))


# print("Smallest number is:", smallest(numbers))



def palindrome(s):
    if len(s)<=1:
        return True
    else:
        if s[0]!=s[-1]:
            return False
        return palindrome(s[1:-1])       
        
s=input("Enter the string:")
if palindrome:
    print("palindrome ")
else:
    print("not palindrome")

(palindrome(s))      