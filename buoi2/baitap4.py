'''
cho danh sách friend = [('bob','male'), ('anna','female'), ('john','male')]
cho biết chiều dài của danh sách
lấy ra phần tử đầu, cuối, giữa và kiểm tra kiểu dữ liệu của chúng
lấy ra thông tin của 2 sinh viên cuối cùng
nhập vào tên, giới tính và chèn vào danh sách gồm 2 giá trị (name, gender)
'''

# cho danh sách friend = [('bob','male'), ('anna','female'), ('john','male')]
friend = [('bob','male'), ('anna','female'), ('john','male')]
print(friend)

# cho biết chiều dài của danh sách
friend_len = len(friend)
print(f'chieu dai cua danh sach: {friend_len}')

# lấy ra phần tử đầu, cuối, giữa và kiểm tra kiểu dữ liệu của chúng
friend1 = friend[0]
friend2 = friend[1]
friend3 = friend[2]
print(f'kieu du cua phan tu dau: {type(friend1)}, kieu du lieu phan tu cuoi: {type(friend3)}, kieu du lieu phan giua: {type(friend2)}')

# lấy ra thông tin của 2 sinh viên cuối cùng
friend = [('bob','male'), ('anna','female'), ('john','male')]
del friend[0]
print(friend)

# nhập vào tên, giới tính và chèn vào danh sách gồm 2 giá trị (name, gender)
friend = [('bob','male'), ('anna','female'), ('john','male')]
name= str(input('nhap name: '))
gender= str(input('nhap gender: '))
friend_info = (name, gender)
friend.append(friend_info)
print(friend)