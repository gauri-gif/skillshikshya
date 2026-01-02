#lamda function
# lambda x,y:x+y
# #assigning lambda function to a variable 
# add= lambda x,y:x+y
# #using the lambda function 
# result=add(5,6)
# print(result)
# print(type(add))


#using lambda function with map
# numbers=[1,2,3,4]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)

# even = lambda x: "Even" if x % 2 == 0 :
# else "Odd"
# print(even(7))   

even=lambda x:"even"if x%2==0 else "odd"
print(even(7))



