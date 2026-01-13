# Higher Order Function (Decorator)


# def show_operator(func):
#     def wrapper(a, b):
#         print("Operator: Addition")
#         return func(a, b)
#     return wrapper


# @show_operator
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print("Result:", result)


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("before function call")
#         func(*args ,**kwargs)
#         print("after  function call")
#         return "done"
#     return wrapper
# @my_decorator
# def my_function():
#     print("Inside function")


# print(my_function())    





# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before addition")
#         func(*args, **kwargs)
#         print("After addition")
#         return "Addition Done"
#     return wrapper


# @my_decorator
# def add(a, b):
#     print("Inside function: Result =", a + b)

# print(add(5, 3))


#create a decorator that filter out the duplicate values from the list and use that decorator in a function to find the maximum value from the list 
# Decorator to remove duplicates from a list



def remove_duplicates(func):
    def wrapper(lst):
        new_list = list(set(lst))
        return func(new_list)
    return wrapper
@remove_duplicates
def find_max(lst):
    return max(lst)
    
my_list = [1, 2, 3, 4, 5, 3, 2, 5,10,10,30,30,30]

result = find_max(my_list)
print("Maximum value:", result)
