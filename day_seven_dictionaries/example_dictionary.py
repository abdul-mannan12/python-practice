dct = dict()
print(type(dct))

person = {
    'name':'Raza',
    'age':23,
    'city':'Sargodha',
    'subject':['scrience','English','Maths'],
    'is_married':False,
    'address':{
        'Area':'Gillwala',
        'street':4
    }
    
}

#adding a key with value
person['country'] = 'Pakistan'

#modify
person['name'] = 'Sami'

#remove the key with theor value
person.pop('is_married')

# #change dict to list
# print(person.items())

#adding in subject
# person['subject'].append('Computer Science')
person['subject'].extend(['Computer','Urdu'])

# key as list
print(person.keys(),'\n')

# keys and their valuse as tuples
print(person.items(), '\n')


for per in person:
    # print(person[per])
    print(per,':', person.get(per))