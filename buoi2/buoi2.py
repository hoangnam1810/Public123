# print("hello")
'''
    ôn tập
    nhập vào tên, tuổi của 1 sinh viên:
    - in ra màn hình tên và tuổi của sinh viên đó
    - kiểm tra kiểu dữ liệu của 2 biến tên tuổi và in ra trên 1 dòng cách nhau bởi dấu ,
    - định nghĩa cho 2 biến num1 num2 có cùng giá trị bất kì, kiểm tra 2 biến đó thuộc kiểu dữ liệu gì
'''

# nhập vào tên, tuổi của 1 sinh viên
name = input("nhap ten: ")
age = int(input("nhap tuoi: "))

# in ra màn hình tên và tuổi của sinh viên đó
print("sinh vien ten: {} ,tuoi: {} ".format(name,age))
print(f"sinh vien ten: {name}, tuoi: {age}")

# kiểm tra kiểu dữ liệu của 2 biến tên tuổi và in ra trên 1 dòng cách nhau bởi dấu ,
type_a = type(name)
type_b = type(age)
print(type_a, type_b)

# định nghĩa cho 2 biến num1 num2 có cùng giá trị bất kì, kiểm tra 2 biến đó thuộc kiểu dữ liệu gì
num1 = num2 = 1
print(type(num1))
print(type(num2))


'''
lý thuyết
'''
'''
    list (danh sách)
    phương thức của list: len, min, max, append, extend, remove, pop, del, clear, sort, reverse, sum
    slicing: tìm vị trí
    index
'''

#  list chứa trong cặp dấu ngoặc []

#      0     1       2    3
list = [2, 'hello', 2.1, 5+2j]
print(list)
print(type(list))

# pop(): xóa phần tử cuối cùng trong list
pop = list.pop()
print(pop)
print(list)

# remove(): xóa phần tử trong list
list.remove('hello')
print(list)

list2 = [1, 'ok', 'bro', 34]

# hàm remove() không thể bị chứa trong biến
remove_value = list2.remove('ok')
print(remove_value)
print(list2)

# insert(): dùng để thêm phần tử vào list
# Cú pháp: insert(index, tham số muốn thêm vào)
list3 = [1, 2, 3, 4, 5]
list3.insert(0, 0)
print(list3)

# append(): dùng để thêm phần tử VÀO CUỐI list
list3.append(6)
print(list3)

# extend(): dùng để thêm nhiều phần tử vào danh sách
extend_value = [7, 8, 9]
list3.extend(extend_value)
print(list3)

# extend khác với append và insert ở chỗ nó có thể truyền nhiều tham số vào list
# append: truyền vào cuối
# insert: truyền ở bất cứ vị trí nào mà bạn muốn

# len(): dùng để đếm độ dài của list
len_list3 = len(list3)
print(len_list3)
print(list3)

# min(), max(): tìm phần tử lớn nhất, nhỏ nhất
max_value = max(list3)
min_value = min(list3)
print(max_value)
print(min_value)

'''
    slicing
    list in list
    copy list
    del
'''
# slicing dùng cặp dấu ngoặc vuông []
#           0     1     2     3    4
list4 = ['nam', 'tai', 'tui', 21, 23]
slicing_list = list4[3]
i = int(input('nhap vi tri muon xem gia tri: '))
slicing_list1 = list4[i]
print(f'tại vị trí số {i}, giá trị là {slicing_list1}')

# slicing(start:stop:step)
# nguyên lý: đếm từ vị trí start đến vị trí end NHƯNG KHÔNG LẤY GIÁ TRỊ END MÀ CHỈ LẤY GIÁ TRỊ TRƯỚC END
#           0    1       2    3    4  
#          -5    -4     -3    -2  -1
list4 = ['nam', 'tai', 'tui', 21, 23]
list5 = ['s', 'a', 'b', 'c', 'd', 'h', 'r', 'g']
print(list4[0:4])
print(list4[-3:-1])

# list in list
list1 = [1, 2, 3, 4, 5, 6]
list = list1
print(list is list1)
# trong máy tính có bộ nhớ, list1 nó đang nằm trong bộ nhớ ô thứ 2
# list = list1 list cũng nằm bộ nhớ ô thứ 2
# khi mà thao tác trên list, thì list1 nó cũng thay đổi theo luôn và ngược lại 
list.append(7)
print(list1)

# copy list
list_a = [1, 2, 3, 4, 5, 6]
list_b = list_a.copy()
print(list_b)
list_b.append(7)
print(list_a)
print(list_b)

# del: xóa theo index
list_a = [1, 2, 3, 4, 5, 6]
del list_a[1]
print(list_a)

# clear(): xóa phần tử trong list
list_a = [1, 2, 3, 4, 5, 6]
list_a.clear()
print(list_a)

# count(): đếm phần tử trong list xuất hiện bao nhiêu lần
list_a = [1, 2, 3, 4, 5, 6, 3]
amount = list_a.count(4)
print(f'số 4 xuát hiện {amount} lần trong list_a')

#sum(): tính tổng phần tử trong list
sum_value = sum(list_a)
print(sum_value)

# sort: sắp xếp vị trí từ nhỏ tới lớn
list_a = [1, 23, 5, 7,2,57,8,234]
print(list_a)

# reverse: đảo ngược list
list_a.reverse()
print(list_a[0:-1])









