# bài tập: giải phương trình bậc 2 


from cmath import sqrt


a = int(input('nhap a '))
b = int(input('nhap b '))
c = int(input('nhap c '))
 
delta = pow(b,2) - 4*a*c

if delta > 0:
    x1 = ((-b + sqrt(delta)) / (2*a))
    x2 = ((-b - sqrt(delta)) / (2*a))
    print(f'phuong trinh co 2 nghiem phan biet {x1} va {x2}')

elif delta == 0:
    x1 = x2 = -b/2*a
    print(f'phuong trinh co 2 nghiem kep x1 ={x1} = x2{x2} ')

else:
    print('phuong trinh bac 2 vo nghiem')

print(delta)

# fix nhap
a, b, c = map(eval,input('nhap a, b, c').split())
print(f'phuong trinh bac 2 co dang {a}x^2 +{b}x + c = 0') 
