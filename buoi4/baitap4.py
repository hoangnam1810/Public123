# fix
while True:
    n = int(input('nhap 1 so'))
    dem = 1
    for i in range(2, n+1):
        if n % i ==0:
            dem += 1
    if dem == 2:
        print('la so nguyen to')
    else:
        print('khong phai so nguyen to')

    choice = input('nhap lua chon y/n').strip
    if choice =='y':
        break