'''
set() không chứa phần tử giống nhau
tuple()
join
'''

# ví dụ tuple
tup = 'a','b','c'
tup2 = 'd','e','f'
print(type(tup))
print(tup)

# total index
num = 1, 2, 3, 4, 5, 6, 7
total = tup + tup2
print(total.index('e'))

# set
set = {1,2,3,4,5}
set = set()
print(set)


# set: chỉ chứa các phần tử không trùng lặp với nhau
# add() thêm phần tử vào set
set.add(1)
set.add(1)
set.add(1)
set.add(1)
print(set)

# update() thêm phần tử vào set 
set.update(['nam'])
print(set)

# remove() xóa phần tử trong set (tương tự list)
set.remove(1)
print(set)

# copy set
set2 = set.copy()
print(set2 == set)

# pop (set) xóa đầu
set.update(range(1, 100))
print(set)
pop = set.pop()
print(pop)
print(set)


# set (clear)
set.clear()
print(set)

'''
dictionnary
'''
# import json giúp viết dict đẹp hơn
import json

# dict = {'key' : value}
dict = {'new' : 'nam'}
# lấy keys
x = dict.keys()
print(x)
# lấy value
y = dict.values()
print(y)

# ví dụ dict
dict = {'name' : 'nam',
        'age' : 25,
        'class': 'dth'}
print(dict)
print(json.dumps(dict, indent=4))
n = dict.keys()
print(n)

v = dict.values()
print(v)

# nếu in 1 key không nằm trong dict thì sẽ báo lỗi
'''
ví dụ:
value = dict['id']
print(value)
'''

# thêm key và value vào dict
dict['id'] = '001'
print(json.dumps(dict, indent=4))

# nếu thêm 1 key vào value có sắn ,thì nó sẽ chèn vào vị trí value đó
dict['name'] = 'tu'
print(json.dumps(dict, indent=4)) 

# update(): chèn thêm được nhiều key, value khác nhau
dict.update(gender = 'male', people = 'VietNam')
print(json.dumps(dict, indent=4)) 

# remove, pop, del, popitem
n = dict.pop('people')
print(n)
print(json.dumps(dict, indent=4)) 

# popitem(): xóa đi cặp key, value nằm cuối cùng của dict, kết quả trả về là 1 tuple
pop = dict.popitem()
print(pop)
print(json.dumps(dict, indent=4)) 

# muốn lấy key thì dict.keys, lấy value dict.value
keys = list[dict.keys]
print(keys)

'''
set nâng cao
'''

set1 = {1, 2, 3, 4, 5, 6}
set1 = {1, 2, 4, 7, 9, 16}

# tìm phần tử chung của 2 set
set3 = set1.intersection(set2)
print(set3)

# tìm phần tử khác nhau, có trong set 1 nhưng không có trong set 2
set4 = set1.difference(set2)
print(set4)

# lấy ra phần tử có trong 2 set
set5 = set1.union(set2)
print(set5)

# lấy tất cả có trong 2 set nhưng không lấy số giống nhau trong 2 set
set6 = set1.symmetric_difference(set2)
print(set6)

'''
chú ý !!!
set4 = set1.difference(set2)
print(set1 - set2)
print(set4)

set5 = set1.union(set2)
print(set1 | set2)
print(set5)

set6 = set1.symmetric_difference(set2)
print(set1 ^ set2)
print(set6)
'''

'''
list nâng cao
'''

# điều kiện sử dụng phải là 2 mảng dữ liệu giống nhau (list sum với list , tuple sum với tuple)
lst = [[1, 2, 3, 4],[5, 6, 7, 8]]
total = sum(lst, ['sum'])
print(total)

# join() dùng để chèn với điều kiện phần tử phải chuỗi (str)
# map() dùng để convert 1 biến nào đó thành dữ liệu mong muốn
# lst1 = [1, 2, 3, 4] ==> [1 - 2 - 3 - 4]
lst1 = [1, 2, 3, 4]
x = '-'.join(map(str, lst1))
print(x)

# eval() hàm này dùng để tính toán mà không quan tâm đến kiểu dữ liệu của biến
x = 5
y = 1.5
print(x + y) 