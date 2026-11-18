# multiline
line = '''my name is raaza.
waleed is my friend.
i read in cs department.'''
print(len(line))

print(len('greetings'))

frist_name = 'raza'
last_name = 'waleed'
full_name = frist_name + ' ' + last_name
print(full_name)

#escape sequences
print('name\tage\tcountry\tcity')
print('\"hello\" romi')

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print(f'{a} + {b} = {a + b}')

lang = '    python expert is the best   '
r = "happy,birthdat"
print(lang[::-1])
print(lang.capitalize())
print(lang.find('r'))
print(lang.count('e'))
print(lang.title())
print(lang.swapcase())
print(lang.split())
print(r.split(','))
print(lang[10])
print(lang.find('b'))
print(lang.strip())

