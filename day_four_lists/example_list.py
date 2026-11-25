# Declare a list with more than 5 items
lst = [1,2,3,4,5,2,1,6,7,3,8,1,9,10]

# Find the length of your list
length = len(lst)
print(length)



# Get the first item, the middle item and the last item of the list
first_item = lst[0]
middle_item = lst[length // 2]
last_item = lst[length -1]
print(first_item,middle_item,last_item)

companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
leng = len(companies)
print(leng)

first_company = companies[0]
middle_company = companies[leng // 2]
last_company = companies[leng -1]
print(first_company,middle_company,last_company)

# companies[5] = "Meta"
# print(companies)

# companies[leng // 2 ] = "IT"
# print(companies)
company = []
for val in companies:
    if 'IBM' in val:
        company.append(val)
    else:
        company.append(val.upper()) 
print(company)

# companies.sort()
# print(companies)

# companies.sort(reverse=True)
# print(companies)

# slice = companies[-3:]
# print(slice)

# del companies[0]
# leng -= 1
# del companies[len(companies) // 2]
# leng -= 1
# del  companies[len(companies) -1]

# print(companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
position = full_stack.index('Redux')
full_stack.insert(position + 1, 'Python')
full_stack.insert(position + 2, 'SQL')
print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24 ,6]

sorted_ages = sorted(ages)
print(sorted_ages)

min_age = min(ages)
max_age = max(ages)
print(f"Min age {min_age} \tMax age {max_age}")

# Median 
a , b = sorted_ages[len(sorted_ages) // 2 - 1], sorted_ages[len(sorted_ages) // 2 ]

if len(ages) % 2 == 0:
    median = (a + b) / 2
else:
    median = sorted_ages[len(sorted_ages) // 2 ]

print('Median',median)    

average = round((sum(sorted_ages) / len(sorted_ages)),2)
print('Average',average)

range = max_age - min_age
print('Range',range,'\n')

min_diff = abs(min_age - average)
max_diff = abs(max_age - average)

print(f"Average: {average}")
print(f"|min - average|: {min_diff}")
print(f"|max - average|: {max_diff}")



