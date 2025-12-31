#map
# numbers = [1, 2, 3, 4]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)


# def square(num):
#     return num**2
# numbers=[1,2,3,4]
# squared_numbers=list(map(square,numbers))
# print(squared_numbers)




# numbers=[1,2,3,4,5]

# squares=list(map(lambda  x:x**2,numbers))

# print(squares)

# numbers=[1,2,3,4]

# even_numbers=list(map(lambda x:x%2==0,numbers))
# print(even_numbers)


# def even(num):
#     return num%2==0
# numbers=[1,2,3,4]
# even_numbers=list(map(even,numbers))
# print(even_numbers)



#take  alist make them upper case using higher order builtin function using map
# def upper (name):
#     return name.upper()

# name=["gauri","aarju","janakaa"]
# upper_case=list(map(upper,name))
# print(upper_case)

#find the sum of nested list and return true or false if sum is greater than 10 using  map function

# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# total_sum=map(sum,nested_list)
# print(list(total_sum))



# def sum_num(num):
#     if num>10:
#         return True
#     else:
#         return False
    
# nested_list= [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# total_sum=list(map(sum_num,nested_list))
# result=total_sum>10
# print(result)




# def sum_num(num):
#     return num > 10

# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# total = sum(map(sum_num, nested_list))
# result = sum_num(total)

# print(result)


#filter out the words which have length greater than 3


# words = ["cat", "apple", "dog", "banana", "sun"]

# result = list(filter(lambda word: len(word) > 3, words))
# print(result)




# def length_greater_than_3(word):
#     return len(word) > 3

# words = ["cat", "apple", "dog", "banana", "sun"]

# filtered_words = list(filter(length_greater_than_3, words))
# print(filtered_words)




# def length_greater_than_3(word):
#     return len(word)>3
# words=["cat", "apple", "dog", "banana", "sun"]

# filteres_words=list(filter(length_greater_than_3,words))
# print(filteres_words)


#filter out the dictionary items based on some condition like "name" key length greater than 5

# data=[
#     {'name':'gauri','age':24},
#     {'name':'janakaa','age':24},
#     {'name':'aarju','age':25}

# ]
# def name_length(item):
#     return len(item['name'])>5
# filtered_data=filter(name_length,data)
# print(list(filtered_data))




# def key_length_greater_than_3(item):
#     key, value = item
#     return len(key) > 5

# data = {
#     "name": "gauri",
#     "age": 24,
#     "address": "Dang"
# }

# filtered_dict = dict(filter(key_length_greater_than_3, data.items()))
# print(filtered_dict)




# from functools import reduce

# def add(a, b):
#     return a + b

# numbers = [1, 2, 3, 4]

# result = reduce(add, numbers)
# print(result)


# from functools import reduce

# def longest_word(a, b):
#     if len(a) > len(b):
#         return a
#     else:
#         return b

# words = ["cat", "elephant", "dog", "giraffe"]

# result = reduce(longest_word, words)
# print(result)












  


from functools import reduce
def find_maximum(a,b):
    if a > b:
        return a
    else:
        return b

numbers = [12, 5, 30, 8, 20]

result=reduce(find_maximum,numbers)
print(result)










#reduce

# from functools import reduce

# numbers = [1, 2, 3, 4]
# total = reduce(lambda a, b: a + b, numbers)
# print(numbers)