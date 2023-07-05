""" 
bài tập: nhập vào 1 năm bất kì, kiểm tra xem năm đó có phải năm nhuận hay không? 
biết rằng năm nhuận là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400
 """

year = int(input('nhap nam: '))

if year % 4 == 0:
    print('nam nhuan')
else:
    print('nam thuong')


