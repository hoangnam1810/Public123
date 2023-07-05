'''
câu điều kiện if - else - elif
vòng lập for
vòng lập while
pass, break
'''

# ví dụ 1 if - else 
a = 5
if a %2 == 0:
    print('a chia het cho 2')
else:
    print('a ko chia het cho 2')

# ví dụ 2 
weather = input('nhap thoi tiet')
if weather != 'nang':
    print('mua')
else:
    print('lam ram')

# ví dụ elif
dtb = float(input('nhap diem trung binh'))

if dtb >= 8:
    print('gioi')
elif dtb >=6.5 and dtb < 8:
    print('kha')
else:
    print('tb')

# ví dụ 1 for
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# ví dụ 2 
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
    else:
        print(i, end = ', ')

# ví dụ 3
str = 'lequangtu'

for i in str:
    print(i, end = ' ')

# i là hàng, j là cột trong vòng lập lồng nhau
# ví dụ vẽ chữ N
n = int(input('nhap chieu cao'))

for i in range(n):
	for j in range(n):
		if j==0 or i == j or j==n-1:
			print('*', end = ' ')
		else:
			print(" ", end = ' ')
	print()

# ví dụ vẽ tam giác:
n = int(input('nhap chieu cao'))

for i in range(n):
	for j in range(n):
		if j==0 or i == j or i==n-1:
			print('*', end = ' ')
		else:
			print(" ", end = ' ')
	print()