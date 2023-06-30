import json
dict = {'name' : 'nam',
        'age' : 25,
        'class': 'dth'}
dict['age'] = '28'
print(json.dumps(dict, indent=4)) 

dict.update(gender = 'male', people = 'VietNam')
print(json.dumps(dict, indent=4)) 

n = dict.pop('people')
print(n)
print(json.dumps(dict, indent=4)) 