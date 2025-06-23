person={
    'name':'Vishal khokar',
    'age':27,
    'city':'Pune',
    'email':'vishalkhokar96@gmail.com'
}
person['age']=29
print(person)
if 'email' in person:
   del person['email']

print(person)