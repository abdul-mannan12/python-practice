age = int(input("Enter Your Age: "))

if age >= 18:
    print('You are Eligible for Driving')
else:
    print(f'Your need {18 - age} years for drive')    


month = input("Enter the Month: ").lower().rstrip()

if month in ('september', 'october', 'november'):
    print("Autumn Season")
elif month in ('december', 'january', 'february'):
    print('Winter season')    
elif month in ('march', 'april', 'may'):
    print('Spring season')
elif month in ('june','july','auguest'):
    print('Summer Season') 
else:
    print("in-correct input")    


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
val = person['skills']
if  'skills' in person:
    print(person['skills'][len(val) // 2])
    if 'Python' in person['skills']:
        print('yes')
    else:
        print('No')    

if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('frontend-developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('Backend-developer')  
elif 'JavaScript' in person['skills'] and 'React' in person['skills'] and 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('fullstack developer')
else:
    print('nothing')    


# skills = set(person['skills'])

# if {'JavaScript', 'React', 'Node', 'Python', 'MongoDB'}.issubset(skills):
#     print('fullstack developer')
# elif {'JavaScript', 'React'}.issubset(skills):
#     print('frontend-developer')
# elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
#     print('Backend-developer')
# else:
#     print('nothing')

if person['is_married'] and 'Finland' in person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is Married')

    