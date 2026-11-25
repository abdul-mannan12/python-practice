tpl = ()
names = ('ali','waleed','raza')
girls = ('samreen','warda','romi')
names += girls 
print(len(names))
print(names)

names = list(names)
names[3] = 'abdullah'
print(names,'\n')
names = tuple(names)
print(names)

friend = names[3:]
print(friend,'\n')

veges = ('mirch','tomato','potato')
fruits = ('apple','mangoes','banana')
food_stuff = veges + fruits
print(food_stuff,'\n')

print('apple'in food_stuff,'\n')

food_stuff = list(food_stuff)
first_three = food_stuff[0:3]
print(first_three)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Iceland' in nordic_countries )
