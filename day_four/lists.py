# lst1 = list(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
# print(lst1)

# web_tech = ['python','raza','java','c++']
# print(web_tech,len(web_tech))

# fruits =list(['apple','banana','mango'])
# print(f"{fruits} length of list is {len(fruits)}")


lst = ['moday',123, True , {'name':'raza','age':23}, [1,2,3,4],"123.33",'my name is mani','happy']
# for i in lst:
#     print(i)

# #slicing of list       
# print('\n')
# print(lst[0:3])
# print(lst[1:])
# print(lst[::-1]) 

# #unpacking of list
# print('\n')
# day, number, boolean, dictionary, *rest, string, mood = lst
# print(rest)
# print(day)
# print(number)
# print(boolean)
# print(dictionary)
# print(string)
# print(mood)

# modifing the list
# print('\n')

# lst[0] = 'sunday'
# print(lst)
# lst[1] = 345
# print(lst)
# lst.pop()
# print(lst)

# lst.append('romi')
# print(lst)

# # checking the list

# val =  'romi' in lst
# print(val)

# # Inserting Items into a List

# lst.insert(3, "hello world")
# print(lst)


# # reomve the item from the list

# lst.remove('hello world')
# print(lst)

# deleting the item from the list
del lst[5]
print(lst)

# del lst


# lst.clear()
# print(lst)

print('\n')

# copy al ist
# lst2 = lst
# # print(lst2)

# lst2.append('new item')
# print(lst2)
# print(lst)

# using the copy method

lst3 = lst.copy()
print(lst3)

lst4 = ['new item', 'new item2']

lst5 = lst3 + lst4
lst3.extend(lst4)
print(lst3)
print(lst5)

lst6 = [1,2,3,4,5,6,7,7,6,8,9,10]
c = lst6.count(6)
sorted_list = sorted(lst6)
print(sorted_list)
sum = sum(lst6)
print(sum)
print(c)