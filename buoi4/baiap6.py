n = int(input("nhap so can tinh giai thua: "))

p = 0
s = 1
for i in range(1, n+1):
    s = s* i
    p += 1 / s
print(f'giai thua la {s}')
