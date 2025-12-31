

# dict={"name":"Gauri", "age":24}
# print(dict)
# print(dict.keys())
# print(dict.values())  
# print(dict.items())

# for key,value in dict.items():

    
    # print(key,value)

#accessing elements from dictonary

# name=dict['name']


# dict_1={"name":"gauri", "class":10}

# dict_2={ "age":24,"name":"efgh"}
# print(dict_1==dict_2)
# print(id(dict_1))
# print(id(dict_2))
# print(dict_1 is dict_2)


#merging dictionaries
#1. union merge
# result_dict=dict_2|dict_1
# print(result_dict)
# print(id(result_dict))

#2.update merge

# dict_1.update (dict_2)
# print(dict_1)



# #keyword argument merge

# result_dict={**dict_1,**dict_2}
# print(result_dict)

# result_dict={**dict_2,**dict_1}

# print(result_dict)


#removing key value pair 
dict_3={"name":"gauri","age":24}
# value=dict_3.pop("name")
# print(value)
# print(dict_3)


value=dict_3.popitem()
print(value)
print(dict_3)


#key value

dict_3["name"]="Janaka"
print(dict_3)

print(id(dict_3))