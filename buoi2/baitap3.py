'''
cho danh sách student = [['sv001','bob', 25], ['sv002','kenny', 29], ['sv003','anne', 31]]
lấy thông tin của sinh viên thứ nhất và in ra dưới định dạng: ID: {id}, name: {name}, age: {age}
lấy ra tuổi của sinh viên thứ 2
lấy ra thông tin của 2 sinh viên cuối cùng
lấy ra id của sinh viên thứ 3
'''

# cho danh sách student = [['sv001','bob', 25], ['sv002','kenny', 29], ['sv003','anne', 31]]
student = [['sv001','bob', 25], ['sv002','kenny', 29], ['sv003','anne', 31]]
print(student)

# lấy thông tin của sinh viên thứ nhất và in ra dưới định dạng: ID: {id}, name: {name}, age: {age}
id = student[0][0]
name = student[0][1]
age = student[0][2]
print(f'id: {id}, name: {name}, age: {age}')

# lấy ra tuổi của sinh viên thứ 2
age_2 = student[1][2]
print(f'tuoi sinh vien thu 2: {age_2}')

# lấy ra thông tin của 2 sinh viên cuối cùng
student = [['sv001','bob', 25], ['sv002','kenny', 29], ['sv003','anne', 31]]
del student[0]
print(student)

# lấy ra id của sinh viên thứ 3
student = [['sv001','bob', 25], ['sv002','kenny', 29], ['sv003','anne', 31]]
id_3 = student[2][0]
print(f'id cua sinh vien thu 3: {id_3}')