'''
file
csv
json
'''

# file: open file, process, close
'''
# open file
# tạo file txt trước
file = open('test.txt','r')

# read file
data = file.read()
# print(data)

lst = [line.strip() for line in data] 
print(*lst)

# mở file phải đóng file
file.close()
'''
# r = read, w = write, a = append
# lấy từng dòng readlines
# for line  

with open ('test.txt', mode ='r') as file:
    data = file.read()

print(data)


# ghi file 
with open('test.txt', 'w') as file:
    file.write()

# chèn dữ liệu vào file
with open(file, 'a') as file:
    file.write()

# next(file) bỏ hàng đầu

