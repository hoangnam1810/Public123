x = int(input('nhap x: '))
n = int(input('nhap n: '))

tong = 0

for i in range(1, n+1):
    tu = x**i
    mau = 1
    for j in range(1, i+1):
        mau *= j
    tong += (tu/mau)

print(tong)
