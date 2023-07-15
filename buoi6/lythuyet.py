# '''
# hàm
# '''
# # cú pháp
# '''
# def tên hàm(tham số)
#     khối lệnh
# '''
# def tong(a, b):
#     s = a + b
#     return s
# print(tong(2, 3))

# '''
# biến local và biến global
# '''
# # biến local chỉ ở trong hàm
# # biến global nằm ngoài hàm
# s = 20

# def hieu(a ,b):
#     global s
#     s = s- (a+b)

# hieu = hieu(2,3)
# print

# def func(lst):
#     if lst [-1]>0:
#         print('lon hon 0')
#         print('xoa bo gia tri cuoi cung')
#         lst.pop()
#     else:
#         print('be hon 0')
#         n = int(input('nhap gia tri muon them vao list: '))
#         print(f'list moi la: {lst}')

#     return lst
# lst = [1,2,3,4,5,6,78]
# print('')


'''def fun(num):
    if num % 2 ==0:
        print(f'so chan')
    else:
        print(f'so le')

n = 2
giatri = fun(n)
print(giatri)
'''

'''def trungbinhcong(day_so):
    return sum(day_so)/len(day_so)
    

day_so = (input('nhap day so'))
dayso = [int(i) for i in day_so.split()]

giatri_trungbinh = trungbinhcong(day_so)
print(giatri_trungbinh)
'''

def songuyento(num):
    dem = 1
    for i in range(2, num+1):
        if num % i ==0:
            dem += 1
    if dem == 2:
        return f'{num} la so nguyen to'
    else:
        return f'{num} khong phai la so nguyen to'
    
# gọi hàm bằng cách truyền tham số vào hàm (tham số đó phải được định nghĩa trong hàm)
'''
1. viết tên hàm
2. truyền tham số vào hàm
3. in kết quả
'''
so = 5
gia_tri = songuyento(so)
print(gia_tri)

# nhập 1 dãy số bất kỳ sắp xếp tăng dần
def tang_dan(n):
    n.sort()
    return f'{n} sau khi sap xep'

bien = input('nhap day so: ')
day_so = list(map(eval, bien.split()))
print(day_so)
ket_qua = tang_dan(day_so)
print(ket_qua)

