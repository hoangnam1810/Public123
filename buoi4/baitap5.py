# số đối xứng
# nhập n
n = int(input('nhap so '))
flag =True
# chuyển đổi về str (strip là xóa khoảng trống)
n_str = str(n).strip()
# lấy độ dài của number_string
length = len(n_str)
print(length)
# vòng lặp
for i in range (length //2 ):
    if n_str[i] != n_str[length - i - 1]:
        print(f'{n} khong phai la so doi xung')
    else:
        print(f'{n} la so doi xung')
# flag = False
# if flag:
#     
# else:
#     print(f'{n} khong phai la so doi xung')

