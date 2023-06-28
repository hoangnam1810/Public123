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
