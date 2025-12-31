#set and tuple 
# t1=(1,3,4,5)
# t2=("Python",3.12,True)
# print(t1)
# print(t2)

# empty=()
# print(empty)

# print(type(empty))


#single element tuple


# single=(10,)
# print(single)
# print(type(single))

# not_tuple=(10)
# print(not_tuple)
# print(type(not_tuple))


#create a tuple of 10 element 

# element=(0,1,2,2,4,5,6,7,8,9)
# print(element[::2])
#create a tuple of 10 element 
# elements = (0, 1, 2, 2, 4, 5, 6, 7, 8, 9)
# for e in elements:
#     result_tuple=()
#     result_tuple += result_tuple+(e*2,)
# print(result_tuple)    


# create a tuple of 10 elements
# elements = (0, 1, 2, 2, 4, 5, 6, 7, 8, 9)

# result_tuple = ()   

# for e in elements:
#     result_tuple = result_tuple + (e * 2,)

# print(result_tuple)

# tuple=(1,2,3,4)
# tuple.append(5)
# print(tuple)

# e=(1,2,3,[4,5,6],8,9)
# e[3].insert(0, 3)
# print(e)
# print(len(e))

# e = (1, 2, 3, [4, 5, 6], 8, 9)

# e[3].insert(0, 3)

# print(e)
# print(len(e))

# data=((1,2),(3,4),(5,(1,2)))
# print(data[2][1[1]])


# a = [[1, 2], [3, 4]]
# print(a[1][0])


# t = ((1,2),(3,4))
# t[0][0] = 10   it is not valid 



#2 number task 


# numbers = (1, 2, 2, 3, 3, 4, 4, 4, 5)

# result = tuple(set(numbers))
# print(result)


# t = ((10, 20), (30, 40))#tuple 
# print(t[0][1])


# a = [[1,2],[3,4]]
# for i in a:
#     for j in i:
#         print(j)



# a = ([1,2],[3,4])#0 index ma 9 rakhne 
# a[0][0] = 9
# print(a)



# a = [[1,2],[3,4]]   length nikalne 
# print(len(a))





t = ((2,3), (4,3), (1,5))
# flat = ()

# for item in t:
#     flat = flat + item

# print(flat)

 

flattened_tuple= tuple(element for inner_tuple in t for element in inner_tuple)

print(flattened_tuple)