dict1 = {
        'Fname': 'Jane',
        'Lname': 'Doe',
        'age': 23
        }
print(dict1.get('Fname'))
dict2 = dict1
dict2['age'] = 21
print(dict2)
dict2.update([('occupation', 'student')])
print(dict2)
dict3 = dict2
dict3.pop('Fname')
print(dict3)
print(dict3.values())
dict3.setdefault('hobby', 'chess')
print(dict3)
dict1.clear()
print(dict1)
