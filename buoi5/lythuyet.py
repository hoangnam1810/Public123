'''
zip, enumerate
'''
import json
tup = 'a','b','c'
set = {1,2,3,4,5}
dict = {'new' : 'nam'}
lst = [1, 2, 3, 4]

# zip (phụ thuộc vào ngắn nhất)(!!! muốn in ra phải convert qua dạng khác)
_zip = zip(lst, tup)
print(tuple(_zip))

# enunerate (nó in ra index và giá trị bên trong đó)

'''
list comprehensions
'''

lst=[1, 2, 3, 4]

new_lst=[]
for i in lst:
    tong = i*2
    new_lst.append(v)
print(new_lst)

# compre
'''
1. tạo 1 iterable
2. định nghĩa 1 biến bất kì
3. biểu thức
'''
new_lst1 = [a*2 for a in lst]
print(new_lst1)

# set compre
_set = {'b','u','c'}

new_set = set()
for c in _set:
    h = c.upper()
    new_set.add(h)
print(new_set)

#compre
new_set1 = {s.upper() for s in _set}
print(new_set1)

# dict compre
dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

for key in dict:
    dict[key] *=2
print(json.dumps(dict,indent=4))

# compre
new_dict = {
    k: v*2 for k,v in dict.items()
}
print(json.dumps(new_dict, indent=4))

